from modules import *

class viewOrdersHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			orders=yield db.order_temp.find().to_list(None)
			self.render('viewOrders.html',orders=orders,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		