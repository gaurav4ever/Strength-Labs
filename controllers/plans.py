from modules import *

class monthly_plan_shreddingHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/shredding.html')

class monthly_plan_shredding_veg_eggHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/shredding_veg_egg.html')

class monthly_plan_non_vegshreddingHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/shredding_non_veg.html')

class monthly_plan_bulkingHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/bulking.html')

class monthly_plan_bulking_veg_eggHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/bulking_veg_egg.html')

class monthly_plan_bulking_non_vegHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/bulking_non_veg.html')

class monthly_plan_fat_lossHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/fat_loss.html')

class monthly_plan_fat_loss_veg_eggHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/fat_loss_veg_egg.html')

class monthly_plan_fat_loss_non_vegHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/fat_loss_non_veg.html')

class monthly_plan_customHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/custom.html')