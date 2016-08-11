from modules import *

class recent_ordersHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/recent_orders.html')