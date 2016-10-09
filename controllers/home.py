'''
Preset controller by torn for / route
'''
from modules import *
import json
from tornado.escape import json_encode

class homeHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('index.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.render('index.html', result = dict(loggedIn=False))

class macro_calHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/macro_cal_form.html')

class plan_formHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render('data/meal_form.html')

class faqHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
			self.render('faq.html')

class req_msgHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		name=self.get_argument('q_name')
		email=self.get_argument('q_email')
		msg=self.get_argument('q_message')
		request_msg={
			'name':name,
			'email':email,
			'msg':msg
		}
		yield db.req_messages.insert(request_msg)
		self.redirect('/?message=true')

class terms_privacyHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('termsAndPrivacy.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.render('termsAndPrivacy.html',result = dict(loggedIn=bool(self.get_secure_cookie('user'))))

class info_pageHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('info_page.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.render('info_page.html',result = dict(loggedIn=bool(self.get_secure_cookie('user'))))

class reqHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		self.render("info_page.html")
		# users=yield db.users.find().to_list(None)
		# a={}
		# for i in users:
		# 	b={
		# 		"username":i["full_name"]+""+i["last_name"],
		# 		"password":i["password"],
		# 		"email":i["email"],
		# 		"mobile":i["mobile"]
		# 	}
		# 	self.write(b)
		# 	self.set_header("Content-Type", "application/json")

class apiAccountsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self,user_id):
		users=yield db.users.find_one({'_id':ObjectId(user_id)})
		b={
			"id":str(users['_id']),
			"name":users["full_name"]+" "+users["last_name"],
			"password":users["password"],
			"email":users["email"],
			"mobile":users["mobile"]
		}
		# self.write(b)
		self.write(json.dumps(b, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")

	# def post(self,user_id):
	# 	name=self.get_argument('user_name')
	# 	users=yield db.users.find_one({'full_name':name})
	# 	b={
	# 		"id":str(users['_id']),
	# 		"name":users["full_name"]+" "+users["last_name"],
	# 		"password":users["password"],
	# 		"email":users["email"],
	# 		"mobile":users["mobile"]
	# 	}
	# 	# self.write(b)
	# 	self.write(json.dumps(b, sort_keys=True,indent=4, separators=(',', ': ')))
	# 	self.set_header("Content-Type", "application/json")

class apiOrdersHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self,orderId):
		user_order=yield db.order_temp.find_one({'_id':ObjectId(orderId)})
		b={
			"orderId":str(user_order['_id']),
			"username":user_order["user_name"],
			"customerID":user_order["user_id"],			
			"EmailID":user_order["user_mail"],
			"DeliveryTime":user_order['time'],
			"TotalFreq":user_order['Tmeal_freq'],
			"MealFreqRem":user_order['meal_freq'],
			"Location":user_order['location'],
			"userImg":user_order['user_img'],
			"specification":user_order['specification']
		}
		# self.write(b)
		self.write(json.dumps(b, sort_keys=True,indent=4, separators=(',', ': ')))
		self.set_header("Content-Type", "application/json")	

		# def post(self):
		# 	name=self.get_argument('user_name')
		# 	user_order=yield db.order_temp.find_one({'user_name':name})
		# 	b={
		# 		"orderId":str(user_order['_id']),
		# 		"username":user_order["user_name"],
		# 		"customerID":user_order["user_id"],			
		# 		"EmailID":user_order["user_mail"],
		# 		"DeliveryTime":user_order['time'],
		# 		"TotalFreq":user_order['Tmeal_freq'],
		# 		"MealFreqRem":user_order['meal_freq'],
		# 		"Location":user_order['location'],
		# 		"userImg":user_order['user_img'],
		# 		"specification":user_order['specification']
		# 	}
		# 	# self.write(b)
		# 	self.write(json.dumps(b, sort_keys=True,indent=4, separators=(',', ': ')))
		# 	self.set_header("Content-Type", "application/json")

class apiBillsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self,orderID):
			bills=yield db.bills.find({'order_id':orderID}).to_list(None)
			for bill in bills:
				b={
					"name":bill['user_name'],
					"billID":bill['bill_id']
				}
				# self.write(b)
				self.write(json.dumps(b, sort_keys=True,indent=4, separators=(',', ': ')))
				self.set_header("Content-Type", "application/json")

	# def post(self):
	# 	orderID=self.get_argument('user_name')
	# 	bills=yield db.bills.find({'order_id':orderID}).to_list(None)
	# 	for bill in bills:
	# 		b={
	# 			"name":bill['user_name'],
	# 			"billID":bill['bill_id']
	# 		}
	# 		# self.write(b)
	# 		self.write(json.dumps(b, sort_keys=True,indent=4, separators=(',', ': ')))
	# 		self.set_header("Content-Type", "application/json")
















