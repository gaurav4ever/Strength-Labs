from modules import *

class ordersHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			user_id = self.get_secure_cookie('user')
			result=yield db.users.find_one({'_id':ObjectId(user_id)})
			cartitems = yield db.cart.find({'user':user_id}).to_list(None)
			finalcart = {}
			price={}
			if bool(cartitems):
				for i in range(len(cartitems)-1):
					if cartitems[i]['food_id'] not in finalcart.keys():
						finalcart[cartitems[i]['food_id']] = 1
						for j in range(i+1,len(cartitems)):
							if cartitems[i]['food_id'] == cartitems[j]['food_id']:
								finalcart[cartitems[i]['food_id']] = finalcart[cartitems[i]['food_id']] + 1
				
				if cartitems[len(cartitems)-1]['food_id'] not in finalcart.keys():
					finalcart[cartitems[len(cartitems)-1]['food_id']] = 1
					price[cartitems[len(cartitems)-1]['food_id']]=1

				dp=0

				total_price=0
				for i in finalcart:
					res = yield db.food.find_one({'_id':ObjectId(i)})
					# print res['DP']
					finalcart[i] = {'Quantity':finalcart[i],'Details':res}
					
					p=int(finalcart[i]['Details']['price'])
					dp_limit=finalcart[i]['Details']['DP']*finalcart[i]['Quantity']
					dp+=dp_limit
					final_price=p*finalcart[i]['Quantity']
					total_price+=final_price

				for i in finalcart:
					print finalcart[i]['Details']['food_name']
					print finalcart[i]['Quantity']

					price[i]={'final_price':final_price}

				self.render('orders.html', finalcart = finalcart,price=price,result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
			else:
				self.render('orders.html', finalcart = finalcart,price=price,result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.render('orders.html',result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))


	