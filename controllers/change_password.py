from modules import *

class change_passwordHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			result=yield db.users.find_one({'_id':ObjectId(id)})
			self.render('data/change_pass.html',result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class changepasswordHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		old_pass=self.get_argument('old_pass')
		new_pass=self.get_argument('new_pass')
		conf_new_pass=self.get_argument('conf_new_pass')

		old_pass_check=yield db.users.find_one({'password':old_pass})

		if bool(old_pass_check):
			#checking if new password and confirm new password is correct
			if new_pass==conf_new_pass:
				db.users.update({'password':old_pass},{'$set':{'password':new_pass}})
				self.redirect('/change_pass?passwordchanged=true')
			else:
				self.redirect('/change_pass?new_and_conf_password_match=false')	
		else:
			self.redirect('/change_pass?old_password_match=false')