from modules import *

class mealsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('meals/meals.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.render('meals/meals.html',result = dict(loggedIn=bool(self.get_secure_cookie('user'))))

class vegHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			veg_meal_bulking=yield db.veg_meal.find({'program':'bulking'}).to_list(None)
			veg_meal_shredding=yield db.veg_meal.find({'program':'shredding'}).to_list(None)
			custom_meals=yield db.veg_meal.find({'type':'custom'}).to_list(None)
			self.render('meals/veg.html',custom_meals=custom_meals,veg_meal_bulking=veg_meal_bulking,veg_meal_shredding=veg_meal_shredding,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			veg_meal_bulking=yield db.veg_meal.find({'program':'bukling'}).to_list(None)
			veg_meal_shredding=yield db.veg_meal.find({'program':'shredding'}).to_list(None)
			custom_meals=yield db.veg.find({'type':'custom'}).to_list(None)
			self.render('meals/veg.html',custom_meals=custom_meals,veg_meal_bulking=veg_meal_bulking,veg_meal_shredding=veg_meal_shredding,result = dict(loggedIn=bool(self.get_secure_cookie('user'))))


class nonvegHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			nonveg_meal_bulking=yield db.nonveg_meal.find({'program':'bulking'}).to_list(None)
			nonveg_meal_shredding=yield db.nonveg_meal.find({'program':'shredding'}).to_list(None)
			custom_meals=yield db.nonveg_meal.find({'type':'custom'}).to_list(None)
			self.render('meals/nonveg.html',custom_meals=custom_meals,nonveg_meal_shredding=nonveg_meal_shredding,nonveg_meal_bulking=nonveg_meal_bulking,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			nonveg_meal_bulking=yield db.nonveg_meal.find({'program':'bulking'}).to_list(None)
			nonveg_meal_shredding=yield db.nonveg_meal.find({'program':'shredding'}).to_list(None)
			custom_meals=yield db.nonveg_meal.find({'type':'custom'}).to_list(None)
			print custom_meals
			self.render('meals/nonveg.html',custom_meals=custom_meals,nonveg_meal_shredding=nonveg_meal_shredding,nonveg_meal_bulking=nonveg_meal_bulking,result = dict(loggedIn=bool(self.get_secure_cookie('user'))))


class eggHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			egg_meal_bulking=yield db.egg_meal.find({'program':'bulking'}).to_list(None)
			egg_meal_shredding=yield db.egg_meal.find({'program':'shredding'}).to_list(None)
			custom_meals=yield db.egg_meal.find({'type':'custom'}).to_list(None)
			self.render('meals/egg.html',custom_meals=custom_meals,egg_meal_shredding=egg_meal_shredding,egg_meal_bulking=egg_meal_bulking,result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			egg_meal_bulking=yield db.egg_meal.find({'program':'bulking'}).to_list(None)
			egg_meal_shredding=yield db.egg_meal.find({'program':'shredding'}).to_list(None)
			custom_meals=yield db.egg_meal.find({'type':'custom'}).to_list(None)
			self.render('meals/egg.html',custom_meals=custom_meals,egg_meal_shredding=egg_meal_shredding,egg_meal_bulking=egg_meal_bulking,result = dict(loggedIn=bool(self.get_secure_cookie('user'))))

class custom_reqHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			check=yield db.order_temp.find_one({'user_id':str(id)})
			meal_type=self.get_argument('meal_type')
			if(check==None):
				if meal_type=='veg':
					self.redirect('/veg?mealordered=False')
				elif meal_type=='nonveg':
					self.redirect('/nonveg?mealordered=False')
				else:
					self.redirect('/egg?mealordered=False')
			else:
				req_msg=self.get_argument('user_custom_textarea')
				req={
					'meal_type':meal_type,
					'msg':req_msg,
					'name':result['full_name']+" "+result['last_name'],
					'acc_id':result['_id'],
					'mobile':result['mobile']
				}
				yield db.custom_meals.insert(req)
				yield db.order_temp.update(
						{'user_id':str(id)},
						{
							'$set':{
								'specification':req_msg
							}
						}
					)
				if meal_type=='veg':
					self.redirect('/veg?success')
				elif meal_type=='nonveg':
					self.redirect('/nonveg?success')
				else:
					self.redirect('/egg?success')
		else:
			self.redirect('/veg?loggedIn=false')

class bookHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			meal_pack=self.get_argument('meal_pack')
			Tmeal_freq=self.get_argument('freq')
			timing=self.get_argument('timing')
			location=self.get_argument('location')
			meal_freq=Tmeal_freq
			img="default.png"
			a={
				'user_id':str(result['_id']),
				'user_name':result['full_name']+" "+result['last_name'],
				'food_name':meal_pack,
				'user_mail':result['email'],
				'mobile':result['mobile'],
				'Tmeal_freq':Tmeal_freq,
				'meal_freq':meal_freq,
				'time':timing,
				'location':location,
				'user_img':img,
				'specification':"No Specification",
			}
			yield db.order_temp.insert(a)
			if(meal_pack=='nonveg_shredding_meal' or meal_pack=='nonveg_bulking_meal'):
				self.redirect('/nonveg?mealBooked=true')
			elif(meal_pack=='veg_shredding_meal' or meal_pack=='veg_bulking_meal'):
				self.redirect('/veg?mealBooked=true')
			else:
				self.redirect('/egg?mealBooked=true')

		else:
			meal_pack=self.get_argument('meal_pack')
			if(meal_pack=='nonveg_shredding_meal' or meal_pack=='nonveg_bulking_meal'):
				self.redirect('/nonveg?loggedIn=false')
			elif(meal_pack=='veg_shredding_meal' or meal_pack=='veg_bulking_meal'):
				self.redirect('/veg?loggedIn=false')
			else:
				self.redirect('/egg?loggedIn=false')





