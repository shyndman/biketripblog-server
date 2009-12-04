import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

#
# Base class for handlers
#
class HandlerBase(webapp.RequestHandler):
	def write_template(self, values):
		path = os.path.join(os.path.dirname(__file__), 'html/base.html')
		self.response.out.write(template.render(path, values))