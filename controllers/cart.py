from modules import *

"""
{
	"_id",
	"user",
	"food_id",
	"ordered":0 | 1
}
"""


class addcartHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			food_id = self.get_argument('food_id')
			user_id = self.get_secure_cookie('user')
			yield db.cart.insert({'user':user_id,'food_id':food_id,'ordered':0})

	# def get(self):
	# 	if bool(self.get_secure_cookie('user')):
	# 		id=self.get_secure_cookie('user')
	# 		result=yield db.users.find_one({'_id':ObjectId(id)})
	# 		self.render('data/address.html',result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))


class cartHandler(tornado.web.RequestHandler):
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
				self.render('cart.html', finalcart = finalcart,total_price=total_price,price=price,cart=1,dp=dp,result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
			else:
				self.render('cart.html', finalcart = finalcart,price=price,cart=0,result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.render('cart.html',cart=0,result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class coupon_codeHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		code=self.get_argument('coupon')
		discount={}
		get_coupon=yield db.coupons.find_one({'coupen_code':code})
		if bool(get_coupon):
			if get_coupon['isValid'] == "1":
				db.coupons.update(
						{"_id": ObjectId(get_coupon["_id"])},
						{
							"coupen_code":get_coupon['coupen_code'],
							"discount":get_coupon['discount'],
							"isValid":"0"
						}
					)
				self.redirect('/cart?coupon=applied_'+get_coupon['discount'])
			else:
				self.redirect('/cart?coupon=expired')
		else:
			self.redirect('/cart?coupon=invalid')













