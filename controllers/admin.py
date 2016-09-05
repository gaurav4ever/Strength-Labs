from modules import *

class viewOrdersHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			orders=yield db.order_temp.find().to_list(None)
			self.render('admin/viewOrders.html',orders=orders,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class accountsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			users=yield db.users.find().to_list(None)
			self.render('admin/accounts.html',users=users,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class billsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			bills=yield db.bills.find().to_list(None)
			self.render('admin/bills.html',bills=bills,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))	