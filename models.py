from google.appengine.ext import db

class Point(db.Model):
	
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

class BlogPost(db.Model):

	author = db.UserProperty()
	subject = db.StringProperty() 
	content = db.TextProperty()
	date = db.DateTimeProperty(auto_now_add=True)
	published = db.BooleanProperty()