#!/usr/bin/env python
import os
import cgi
import wsgiref.handlers
import models
import bike_pb2
from base import HandlerBase
from datetime import datetime
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import users

#
# Utility function for returning super.
#
def sup(self):
	return super(self.__class__, self)
	
#
# The data upload page
#
class DataUploadHandler(HandlerBase):
	def post(self):
		pbStr = self.request.body
		uploadPkg = bike_pb2.UploadPackage()
		uploadPkg.ParseFromString(pbStr)
		
		self.response.out.write(str(uploadPkg))
		
		for pt in uploadPkg.points:
			model_pt = models.Point(
				id = pt.id, 
				geo_pt = db.GeoPt(pt.latitude, pt.longitude), 
				bearing = pt.bearing,
				temperature = pt.temperature,
				ts = datetime.fromtimestamp(pt.timeStamp)
			)
				
			# Add altitude if we have it
			if pt.HasField('altitude'):
				model_pt.altitude = pt.altitude
				
			# Put the thing in the datastore
			model_pt.put()

#
# This is a KML handler
#
class KmlHandler(HandlerBase):
	def get(self):
		points = db.GqlQuery("SELECT * FROM Point ORDER BY ts")
		
		self.response.headers["Content-Type"] = "application/vnd.google-earth.kml+xml"
		kml = """<?xml version="1.0" encoding="UTF-8"?>
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
				<coordinates>"""
		
		# Print out each of the points (for some reason, lon then lat)
		for pt in points:
			kml += (str(pt.geo_pt.lon) + "," + str(pt.geo_pt.lat) + ",2357\n")
			
		kml += """
				</coordinates>
			</LineString>
		</Placemark>
	</Document>
</kml>"""

		self.response.out.write(kml)
 
#
# Running the application
#
def main():
	application = webapp.WSGIApplication(
		[
			('/kml', KmlHandler),
			('/upload', DataUploadHandler)
		],
		debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()