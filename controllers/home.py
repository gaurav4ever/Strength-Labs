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
		print user_id
		url=self.request.uri
		new_url=url.split("?")
		if len(new_url)==1:
			users=yield db.users.find_one({'_id':ObjectId(user_id)})
			b={
				"id":str(users['_id']),
				"name":users["full_name"]+" "+users["last_name"],
				"email":users["email"],
				"mobile":users["mobile"]
			}
			# self.write(b)
			self.write(json.dumps(b, sort_keys=True,indent=4, separators=(',', ': ')))
			self.set_header("Content-Type", "application/json")
		else:
			#for id 
			new_url_id=new_url[0]
			new_url_id=new_url_id.split("/")
			new_url_id=new_url_id[3]
			
			#for values
			new_url=new_url[1]
			new_url=new_url.split("=")
			new_url=new_url[1]
			new_url=new_url.split(",")
			new_url=sorted(new_url)
			users=yield db.users.find_one({'_id':ObjectId(new_url_id)})
			if len(new_url)==3:
				b={
					"id":new_url_id,
					new_url[0]:users['email'],
					new_url[1]:users['mobile'],
					new_url[2]:users['full_name']+" "+users['last_name']
				}
			elif new_url[0]=='all':
				b={
					"id":str(users['_id']),
					"name":users["full_name"]+" "+users["last_name"],
					"password":users["password"],
					"email":users["email"],
					"mobile":users["mobile"]
				}
			elif len(new_url)==2:
				if new_url[0]=='email' and new_url[1]=='mobile':
					b={
						"id":new_url_id,
						new_url[0]:users['email'],
						new_url[1]:users['mobile'],
					}
				elif new_url[0]=='email' and new_url[1]=='name':
					b={
						"id":new_url_id,
						new_url[0]:users['email'],
						new_url[1]:users['full_name']+" "+users['last_name']
					}
				elif new_url[0]=='mobile' and new_url[1]=='name':
					b={
						"id":new_url_id,
						new_url[0]:users['mobile'],
						new_url[1]:users['full_name']+" "+users['last_name']
					}
			
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
			a=list()
			for bill in bills:
				b={
					"name":bill['user_name'],
					"billID":bill['bill_id']
				}
				a.append(b)
			c={
				"bills":a
			}
			self.write(json.dumps(c, sort_keys=True,indent=4, separators=(',', ': ')))
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

class dytilaMainMenuHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
			a=list()
			b1={
				"MealName":"Dytila Veg Meals",
				"img":"https://dytila.herokuapp.com/static/img/app%20pics/veg_main.png"
			}
			a.append(b1)
			b2={
				"MealName":"Dytila Non-Veg Meals",
				"img":"https://dytila.herokuapp.com/static/img/app%20pics/nonveg_main.png"
			}
			a.append(b2)
			b3={
				"MealName":"Dytila Egg Meals",
				"img":"https://dytila.herokuapp.com/static/img/app%20pics/egg_main.png"
			}
			a.append(b3)
			b4={
				"MealName":"Dytila Shakes",
				"img":"https://dytila.herokuapp.com/static/img/app%20pics/shakes_main.png"
			}
			a.append(b4)
			b5={
				"MealName":"Dytila Cheat Meals",
				"img":"https://dytila.herokuapp.com/static/img/app%20pics/cheat_main.png"
			}
			a.append(b5)
			c={
				"menu":a
			}
			self.write(json.dumps(c, sort_keys=True,indent=4, separators=(',', ': ')))
			self.set_header("Content-Type", "application/json")















