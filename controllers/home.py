'''
Preset controller by torn for / route
'''
from modules import *
import json
from tornado.escape import json_encode

class homeHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('index.html')


class bynowHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		size=self.get_argument("size");
		self.render('bynow.html',size=size)

class orderHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		name=self.get_argument("name");
		email=self.get_argument("email");
		mobile=self.get_argument("mobile");
		size=self.get_argument("size");
		address=self.get_argument("address");
		a={
			"name":name,
			"email":email,
			"mobile":mobile,
			"size":size,
			"address":address
		}

		yield db.slabs.insert(a)

		self.redirect("/?ordered=true")