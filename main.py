#!/usr/bin/env python
import os
import cgi
import wsgiref.handlers
import models
import bike_pb2
import yaml
import logging
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import users

def sup(self):
	'''Utility function for returning super.'''
	
	return super(self.__class__, self)
	
def get_config():
	'''Gets the configuration as a dict'''
	
	config_file = open('config.yaml', 'r')
	return yaml.load(config_file.read())
	
class DataUploadHandler(webapp.RequestHandler):
	'''The data upload page'''
	
	def post(self):
		'''Handles a post message containing a Google Protobuf'''
		
		uploaded_post = self.read_post_from_request(self.request.body)

		post = models.Post(title=uploaded_post.title, body=uploaded_post.body)		
		post.put()
		
		points = []
		for pt in uploaded_post.points:
			points.append(self.add_point(post, pt))
			
		photos = []
		for photo in uploaded_post.photos:
			photos.append(self.add_photo(post, photo))
			
		push_blog_post(post, points, photos)
			
	def push_blog_post(self, post, points, photos):
		pass
			
	def read_post_from_request(self, body):
		'''Reads in a post from the PB'''	
		
		uploaded_post = bike_pb2.Post()
		uploaded_post.ParseFromString(body)		
		
		logging.info("Read %s" % str(uploaded_post))
		
		return uploaded_post
			
	def add_point(self, post, pt):
		'''Adds a point to the datastore'''
		
		model_pt = models.Point(
			id = pt.id, 
			post = post,
			geo_pt = db.GeoPt(pt.latitude, pt.longitude), 
			bearing = pt.bearing,
			temperature = pt.temperature,
			ts = datetime.fromtimestamp(pt.ts)
		)
			
		# Add altitude if we have it
		if pt.HasField('altitude'):
			model_pt.altitude = pt.altitude
			
		# Put the thing in the datastore
		model_pt.put()
		
		return model_pt
			
	def add_photo(self, post, photo):
		'''Adds a photo to the datastore'''
		
		model_photo = models.Photo(
			post = post,
			contents = db.Blob(photo.contents),
			ts = datetime.fromtimestamp(photo.ts)
		)
		
		if photo.HasField('caption'):
			model_photo.caption = photo.caption
			
		model_photo.put()
		
		return model_photo

class KmlHandler(webapp.RequestHandler):
	'''This is a KML handler'''

	def get(self):
		
		if self.request.get('post') == '':
			logger.error("KmlHandler was not provided post parameter")
			return
		
		points = db.GqlQuery("SELECT * FROM Point ORDER BY ts")
		
		self.response.headers["Content-Type"] = "application/vnd.google-earth.kml+xml"
		kml = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
	<Document>
		<Style id="geoPointLine">
			<LineStyle>
				<color>7f0000ff</color>
				<width>4</width>
			</LineStyle>
			<PolyStyle>
				<color>7f000000</color>
			</PolyStyle>
		</Style>
		<Placemark>
			<styleUrl>#geoPointLine</styleUrl>
			<LineString>
				<coordinates>'''
		
		# Print out each of the points (for some reason, lon then lat)
		for pt in points:
			kml += (str(pt.geo_pt.lon) + "," + str(pt.geo_pt.lat) + ",2357\n")
			
		kml += '''
				</coordinates>
			</LineString>
		</Placemark>
	</Document>
</kml>'''

		self.response.out.write(kml)
	
class IndexHandler(webapp.RequestHandler):
	'''Handles the index'''
	def get(self):
		self.response.out.write("up and running!")
		# TODO - Do something cooler here - if only redirect
		
	
def main():	
	'''Runs the app'''
	application = webapp.WSGIApplication(
		[
			('/', IndexHandler),
			('/kml', KmlHandler),
			('/upload', DataUploadHandler)
		],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()