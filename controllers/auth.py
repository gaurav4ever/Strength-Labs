from modules import *

class registerHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		email = self.get_argument('email')
		password = self.get_argument('password')
		fname = self.get_argument('fname')
		lname = self.get_argument('lname')
		mobile = self.get_argument('mobile')
		exists = yield db.users.find_one({'email':email})
		if bool(exists):
			self.redirect('/?alreadyReg=true')
		else:
			print "hello"
			users = {
				'email': email,
				'password': password,
				'full_name': fname,
				'last_name': lname,
				'mobile': mobile,
				'activated':1,
				'DP':100
			}
			yield db.users.insert(users)
			exists = yield db.users.find_one({'email':email,'password':password})
			self.set_secure_cookie('user',str(exists['_id']))
			self.redirect('/')

class loginHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		email = self.get_argument('email')
		password = self.get_argument('password')
		exists = yield db.users.find_one({'email':email,'password':password})
		if bool(exists):
			self.set_secure_cookie('user',str(exists['_id']))
			self.redirect('/')
		else:
			self.redirect('/?login=false')

class logoutHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.clear_cookie('user')
		self.redirect('/')
