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

class user_detailsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			customer_id=self.get_argument('customer_id')
			customer_data=yield db.users.find_one({'_id':ObjectId(customer_id)})
			customer_order_data=yield db.order_temp.find_one({'user_id':customer_id})
			print customer_order_data
			self.render('admin/user_details.html',customer_data=customer_data,customer_order_data=customer_order_data,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))			

class user_billHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			order_id=self.get_argument('order_id')
			bill=yield db.order_temp.find_one({'_id':ObjectId(order_id)})

			#bill generator
			import random
			import datetime
			mydate = datetime.datetime.now()
			day=mydate.strftime("%a")
			date=mydate.strftime("%d")
			month=mydate.strftime("%m")
			today_date=day+date+month
			rand=random.randrange(10000,99999,2)
			bill_id=today_date+str(rand)
			print bill_id
			#end bil generator

			self.render('admin/user_bill.html',bill_id=bill_id,bill=bill,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))			

class udpate_billHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine	
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			bill_id=self.get_argument('bill_id')
			order_id=self.get_argument('order_id')
			bill_details=yield db.order_temp.find_one({'_id':ObjectId(order_id)})
			yield db.order_temp.update(
				{
					'_id':ObjectId(order_id)
				},

					{
						'$set':
							{
								'meal_freq':str(int(bill_details['meal_freq'])-1)
							}
					}
				)
			bill_details=yield db.order_temp.find_one({'_id':ObjectId(order_id)})
			self.render('admin/update_bill2.php',bill_details=bill_details,bill_id=bill_id)

class regularHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			r_orders=yield db.regular.find().to_list(None)
			self.render('admin/regular.html',r_orders=r_orders,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class add_orderHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('admin/add_order.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class add_user_orderHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			name=self.get_argument('user_name')
			meal=self.get_argument('meal_name')
			cost=self.get_argument('cost')
			mobile=self.get_argument('mobile')

			import time;
			time = str(time.asctime( time.localtime(time.time()) ))
			customer={
				'name':name,
				'meal':meal,
				'cost':cost,
				'time':time,
				'mobile':mobile
			}
			yield db.regular.insert(customer)

			self.redirect('/add_order')