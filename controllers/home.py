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
		if bool(self.get_secure_cookie('user')):
			id = self.get_secure_cookie('user')
			result = yield db.users.find_one({'_id':ObjectId(id)})
			a={
				'username':result['full_name']+" "+result['last_name'],
				'email':result['email'],
				'mobile':result['mobile'],
				'password':result['password']
			}
			# print type(json_encode(a))
			self.write(json.dumps(a))
		else:
			self.render('info_page.html',result = dict(loggedIn=bool(self.get_secure_cookie('user'))))	
