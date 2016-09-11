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
			# print customer_order_data
			self.render('admin/user_details.html',customer_data=customer_data,customer_order_data=customer_order_data,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))			

class user_billHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			order_id=self.get_argument('order_id')

			#Can Change
			food=self.get_argument('food')
			mail=self.get_argument('mail')
			mobile=self.get_argument('mobile')
			Tmeal_freq=self.get_argument('Tmeal_freq')
			meal_freq=self.get_argument('meal_freq')
			timing=self.get_argument('timing')
			location=self.get_argument('location')
			img=self.get_argument('img')

			yield db.order_temp.update(
				{
					'_id':ObjectId(order_id)
				},

					{
						'$set':
							{
								'food_name':food,
								'user_mail':mail,
								'mobile':mobile,
								'Tmeal_freq':Tmeal_freq,
								'meal_freq':meal_freq,
								'time':timing,
								'location':location,
								'user_img':img,
							}
					}
				)

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
			bill_detail=yield db.order_temp.find_one({'_id':ObjectId(order_id)})
			yield db.order_temp.update(
				{
					'_id':ObjectId(order_id)
				},

					{
						'$set':
							{
								'meal_freq':str(int(bill_detail['meal_freq'])-1)
							}
					}
				)
			bill_details=yield db.order_temp.find_one({'_id':ObjectId(order_id)})
			self.render('admin/update_bill.html',bill_details=bill_details,bill_id=bill_id)

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
			quantity=self.get_argument('meal_quantity')
			cost=self.get_argument('cost')
			mobile=self.get_argument('mobile')

			import time;
			date = time.strftime("%d/%m/%Y")
			time = time.strftime("%H:%M:%S%p")
			dt=date+" "+time
			customer={
				'name':name,
				'meal':meal,
				'quantity':quantity,
				'cost':cost,
				'time':dt,
				'mobile':mobile
			}
			yield db.regular.insert(customer)

			self.redirect('/add_order')

class update_regularHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		name=self.get_argument('name')
		mobile=self.get_argument('mobile')
		meal=self.get_argument('meal')
		quantity=int(self.get_argument('meal_quantity'))
		cost=self.get_argument('cost')
		# time=self.get_argument('time')
		regular_id=self.get_argument('regular_id')

		yield db.regular.update(
				{
					'_id':ObjectId(regular_id)
				},

					{
						'$set':
							{
								'name':name,
								'mobile':mobile,
								'cost':cost,
								'meal':meal,
								'quantity':quantity,
								# 'time':time
							}
					}
				)
		self.redirect('/regular')

class delete_regularHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		regular_id=self.get_argument('regular_id')
		yield db.regular.remove({'_id':ObjectId(regular_id)})
		self.redirect('/regular')

