from modules import *

class chilli_paneerHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('temp/chilli_paneer.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.redirect('/shop?loggedIn=false')

class boiled_eggsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('temp/boiled_eggs.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.redirect('/shop?loggedIn=false')

class chicken_breastHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('temp/chicken_breast.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.redirect('/shop?loggedIn=false')