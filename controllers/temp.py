from modules import *

class chilli_paneerHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('temp/chilli_paneer.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.redirect('/shop?loggedIn=false')

class boiled_eggsHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('temp/boiled_eggs.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.redirect('/shop?loggedIn=false')

class chicken_breastHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			self.render('temp/chicken_breast.html',result = dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))
		else:
			self.redirect('/shop?loggedIn=false')

class preorderHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			user_id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(user_id)})
			food_name=self.get_argument('food_name');
			name=result['full_name']+" "+result['last_name'];
			order={
				'food_name':food_name,
				'user_id': user_id,
				'user_name':name,
				'user_mail':result['email'],
				'mobile':result['mobile'],
				'Tmeal_freq':'28',
				'meal_freq':'28',
				'time':'4 pm',
				'location':'VIT main gate'
			}
			yield db.order_temp.insert(order)
			if food_name=='chicken breast' :
				self.redirect('/chicken_breast?book=true')
			elif food_name=='chilli paneer' :
				self.redirect('/chilli_paneer?book=true')
			elif food_name=='boiled eggs' :
				self.redirect('/boiled_eggs?book=true')
