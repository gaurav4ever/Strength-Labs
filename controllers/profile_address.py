from modules import *

class profile_addressHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			result=yield db.users.find_one({'_id':ObjectId(id)})
			self.render('data/address.html',result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))