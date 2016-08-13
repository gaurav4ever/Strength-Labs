from modules import *

class custom_plansHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('custom_plans.html')