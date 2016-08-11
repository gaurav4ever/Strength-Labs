from modules import *

class regular_planHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/regular_plan.html')