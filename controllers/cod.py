from modules import *

class codHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/cod.html')