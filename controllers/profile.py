from modules import *

class profileHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			result=yield db.users.find_one({'_id':ObjectId(id)})
			order=yield db.order_temp.find_one({'user_id':id})
			if bool(order)== False :
				order={"food_name":0}
			self.render('profile.html',order=order,result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

# class my_ordersHandler(tornado.web.RequestHandler):
# 	@tornado.gen.coroutine
# 	def get