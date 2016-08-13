'''
Preset controller by torn for / route
'''
from modules import *
class homeHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('index.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.render('index.html', result = dict(loggedIn=False))

class macro_calHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/macro_cal_form.html')

class plan_formHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/meal_form.html')

class faqHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('faq.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))