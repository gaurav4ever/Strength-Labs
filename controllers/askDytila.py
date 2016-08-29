from modules import *

class askDytilaHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		questions=yield db.questions.find().to_list(None)
		# answers=yield db.answers.find().to_list(None)
		askArray=list()
		for i in questions:
			if i['isAnswered']=="1":
				j=yield db.answers.find_one({'que_id':str(i['_id'])})
				a=list()
				a.append(i['question'])
				a.append(i['user_name'])
				a.append(j['answer'])
				a.append(j['user_name'])
				a.append(j['que_id'])
				askArray.append(a)
		self.render("askDytila/indexa.html",askArray=askArray);

class askqueHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			self.render('askDytila/askque.html')
		else:
			self.render('askDytila/askque.html')
			# result=yield db.users.find_one({'_id':ObjectId(id)})
			# self.render('askDytila/askque.html',result=dict(user=result,loggedIn=bool(self.get_secure_cookie('user'))))

class postqueHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			name=yield db.users.find_one({'_id':ObjectId(id)})
			print name['full_name']+name['last_name']
			que=self.get_argument('que')
			que_array={
				"user_id": ObjectId(id),
				"user_name":name['full_name']+" "+name['last_name'],
				"question":que,
				"isAnswered":0,
			}
			yield db.questions.insert(que_array)
			self.redirect("/askque?posted=true")
		else:
			self.redirect("/askque?loggedIn=false")

class ansqueHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		unanswered_questions=yield db.questions.find().to_list(None);
		que=list()
		for i in range(0,len(unanswered_questions)):
			# print unanswered_questions[i]
			if unanswered_questions[i]['isAnswered']=="0" or unanswered_questions[i]['isAnswered']==0:
				a=list()
				a.append(unanswered_questions[i]["user_name"])
				a.append(unanswered_questions[i]["question"])
				a.append(unanswered_questions[i]["_id"])
				a.append(unanswered_questions[i]["user_id"])
				que.append(a)
		# for i in que:
		# 	print "asked by : "+i[0]+" : question"+i[1]
		# # print que
		self.render("askDytila/ansque.html",que=que);

class seemoreHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		a=list()
		que=self.get_argument('que')
		a.append(que)
		askedBy=self.get_argument('askedBy')
		a.append(askedBy)
		ans=self.get_argument('ans')
		a.append(ans)
		answerBy=self.get_argument('answerBy')
		a.append(answerBy)
		q_id=self.get_argument('que_id')
		a.append(q_id)
		#check answers from database
		# print q_id
		getAns = yield db.answers.find({"que_id":q_id}).to_list(None)

		# for i in getAns:
		# 	print i['answer']
		# print getAns
		self.render("askDytila/seeque.html",a=a,getAns=getAns)
	
class ansHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			user_ans=yield db.users.find_one({'_id':ObjectId(id)})
			# print user_ans
			que_id=self.get_argument('ask_id')
			ans=self.get_argument('ans')
			ansToQue={
				"que_id":que_id,
				"answer":ans,
				"user_id": ObjectId(id),
				"user_name": user_ans['full_name']+" "+user_ans['last_name']
			}
			# make the que isAnswered to 1
			yield db.answers.insert(ansToQue)
			ques=yield db.questions.find({'_id':ObjectId(que_id)}).to_list(None)
			yield db.questions.update(
					{'_id':ObjectId(que_id)},
					{
						'$set':{'isAnswered':'1'}
					}
				)
			# print ques
			self.redirect('/ansque')	
		else:
			self.redirect('/ansque?loggedIn=false')

class addansHandler(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def post(self):
		if bool(self.get_secure_cookie('user')):
			id=self.get_secure_cookie('user')
			user=yield db.users.find_one({'_id':ObjectId(id)})
			newAns=self.get_argument('new_ans')
			que_id=self.get_argument('que_id')
			# print user
			# print newAns
			# print que_id
			newAnsDb={
				"que_id":que_id,
				"answer":newAns,
				"user_id": ObjectId(id),
				"user_name": user['full_name']+" "+user['last_name']
			}
			print newAnsDb
			yield db.answers.insert(newAnsDb)
			self.redirect('/askDytila?posted=true')














