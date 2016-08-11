from modules import *

class chat_with_dietitianHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('chat_with_dietitian.html')