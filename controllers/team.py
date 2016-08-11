from modules import *

class teamHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('team.html')