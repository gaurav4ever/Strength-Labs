from modules import *

class shopHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
		vegfood = yield db.food.find({'food_type':'veg'}).to_list(None)
		vegeggfood = yield db.food.find({'food_type':re.compile('egg')}).to_list(None)
		nonvegfood = yield db.food.find({'food_type':'non veg'}).to_list(None)
		smoothies = yield db.food.find({'food_type':'smoothies'}).to_list(None)
		loop=yield db.food.find().to_list(None)
		# for i in range(len(loop)-1):
		# 	print loop[i]['DP']


		# #Dytila Points update function
		# for i in range(len(loop)-1):
		# 	item_price=loop[i]['price']
			
		# 	dp=int(float(item_price)*0.1)
		# 	print item_price
		# 	print dp
		# 	db.food.update(
		# 		{"_id": ObjectId(loop[i]["_id"])},
				
		# 		{
		# 			"food_name":loop[i]['food_name'],
		# 			"food_type":loop[i]['food_type'],
		# 			"description":loop[i]['description'],
		# 			"img name":loop[i]['img name'],
		# 			"price":loop[i]['price'],
		# 			"DP":int(float(item_price)*0.1),
		# 			"macros": {
		# 				        "protein": loop[i]['macros']['protein'],
		# 				        "carbohydrates": loop[i]['macros']['carbohydrates'],
		# 				        "fats": loop[i]['macros']['fats'],
		# 				        "calories": loop[i]['macros']['calories']
		# 				    }
		# 		}

		# 		)

		self.render('shop.html',vegfood = vegfood, vegeggfood = vegeggfood, nonvegfood = nonvegfood, smoothies = smoothies,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))