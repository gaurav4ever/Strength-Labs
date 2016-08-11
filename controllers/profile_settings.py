from modules import *

class profile_settingsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			result=yield db.users.find_one({'_id':ObjectId(id)})
			self.render('data/profile_settings.html',result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class changesettingsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		password=self.get_argument('password')
		password_check=yield db.users.find_one({'password':password})
		email=self.get_argument('email')

		if bool(password_check):
			first_name=self.get_argument('fname')
			last_name=self.get_argument('lname')
			mobile=self.get_argument('mobile_number')
			if bool(self.get_secure_cookie('user')):
				userid=self.get_secure_cookie('user')
				db.users.update(
					{"_id": ObjectId(userid)},
					{
						"password":password,
						"email":email,
						"full_name":first_name,
						"last_name":last_name,
						"mobile":mobile,
						"activated":1
					}
				)
				self.redirect('/profile_settings?saved=true')
		else:
			self.redirect("/profile_settings?password_matched=false")
