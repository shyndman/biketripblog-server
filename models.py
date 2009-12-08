from google.appengine.ext import db

class Post(db.Model):
	'''A blog post'''
	title = db.StringProperty() 
	body = db.TextProperty()
	ts = db.DateTimeProperty(auto_now_add=True)

class Point(db.Model):
	'''A geographical point, associated with a blog post'''
	
	# Reference to the blog post
	post = db.ReferenceProperty(Post)
	
	#required int64 id 			= 1;
	id = db.IntegerProperty()
	
	#optional double latitude 	= 2;
	#optional double longitude 	= 3;
	geo_pt = db.GeoPtProperty()
	
	#optional double altitude 	= 4;
	altitude = db.FloatProperty()
	
	#optional float bearing 		= 5;
	bearing = db.FloatProperty()
	
	#optional float temperature	= 6;
	temperature = db.FloatProperty()
	
	#optional int64 timeStamp 	= 7;
	ts = db.DateTimeProperty()

class Photo(db.Model):
	'''A photo, associated with a blog post'''
	
	# Reference to the blog post
	post = db.ReferenceProperty(Post)
	
	# Caption
	caption = db.StringProperty()
	
	# The bytes of the image
	contents = db.BlobProperty()
	
	# Time the photo was taken
	ts = db.DateTimeProperty()