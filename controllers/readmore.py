from modules import *

class readMore(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		id = self.get_argument('id')
		result = yield db.food.find_one({'_id':ObjectId(id)})
		feedback = yield db.food_feedback.find({'food_id':id}).to_list(length=7)
		self.render('readmore.html',result=result,feedback = feedback, loggedIn = bool(self.get_secure_cookie('user')))

	@tornado.gen.coroutine
	def post(self):
		id = self.get_secure_cookie('user')
		userdets = yield db.users.find_one({'_id':ObjectId(id)})
		feedback = self.get_argument('feedback')
		id = self.get_argument('id')
		yield db.food_feedback.insert({'food_id':id,'username':userdets['full_name']+' '+userdets['last_name'],'feedback':feedback})
		self.redirect('/readmore?id='+id)