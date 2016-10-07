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

class user_billsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			result=yield db.users.find_one({'_id':ObjectId(id)})
			bills=yield db.bills.find({'customer_id':str(id)}).to_list(None)
			user_bill=list()
			for i in bills:
				print i
				if i['bill_id'][0]=='M' and i['bill_id'][1]=='o' and i['bill_id'][2]=='n':
					a= list()
					a.append(i['bill_id'])
					a.append("Monday")
					a.append(i['bill_id'][3]+i['bill_id'][4])
					a.append(i['bill_id'][5]+i['bill_id'][6])
					a.append("2016")
					user_bill.append(a)
				elif i['bill_id'][0]=='S' and i['bill_id'][1]=='u' and i['bill_id'][2]=='n':
					a= list()
					a.append(i['bill_id'])
					a.append("Sunday")
					a.append(i['bill_id'][3]+i['bill_id'][4])
					a.append(i['bill_id'][5]+i['bill_id'][6])
					a.append("2016")
					user_bill.append(a)
				elif i['bill_id'][0]=='T' and i['bill_id'][1]=='u' and i['bill_id'][2]=='e':
					a= list()
					a.append(i['bill_id'])
					a.append("Tuesday")
					a.append(i['bill_id'][3]+i['bill_id'][4])
					a.append(i['bill_id'][5]+i['bill_id'][6])
					a.append("2016")
					user_bill.append(a)
				elif i['bill_id'][0]=='W' and i['bill_id'][1]=='e' and i['bill_id'][2]=='d':
					a= list()
					a.append(i['bill_id'])
					a.append("Wednesday")
					a.append(i['bill_id'][3]+i['bill_id'][4])
					a.append(i['bill_id'][5]+i['bill_id'][6])
					a.append("2016")
					user_bill.append(a)
				elif i['bill_id'][0]=='T' and i['bill_id'][1]=='h' and i['bill_id'][2]=='u':
					a= list()
					a.append(i['bill_id'])
					a.append("Thursday")
					a.append(i['bill_id'][3]+i['bill_id'][4])
					a.append(i['bill_id'][5]+i['bill_id'][6])
					a.append("2016")
					user_bill.append(a)
				elif i['bill_id'][0]=='F' and i['bill_id'][1]=='r' and i['bill_id'][2]=='i':
					a= list()
					a.append(i['bill_id'])
					a.append("Friday")
					a.append(i['bill_id'][3]+i['bill_id'][4])
					a.append(i['bill_id'][5]+i['bill_id'][6])
					a.append("2016")
					user_bill.append(a)
				elif i['bill_id'][0]=='S' and i['bill_id'][1]=='a' and i['bill_id'][2]=='t':
					a= list()
					a.append(i['bill_id'])
					a.append("Saturdat")
					a.append(i['bill_id'][3]+i['bill_id'][4])
					a.append(i['bill_id'][5]+i['bill_id'][6])
					a.append("2016")
					user_bill.append(a)
			self.render('data/user_bills.html',user_bill=user_bill,result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))