from modules import *

class account_settingsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			result=yield db.users.find_one({'_id':ObjectId(id)})
			self.render('data/account_settings.html',result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class deactivate_accountHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		email=self.get_argument('email')
		password=self.get_argument('password')

		old_pass_check=yield db.users.find_one({'password':password})
		if bool(old_pass_check):
			userid=self.get_secure_cookie('user')
			db.users.remove({"_id": ObjectId(userid)})
			self.redirect('/auth/logout')
		else:
			self.redirect('/account_settings?old_password_match=false')