
'''
The main server file
'''
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
import torn
from routes import *
settings = dict(
		template_path = os.path.join(os.path.dirname(__file__), "views"),
		static_path = os.path.join(os.path.dirname(__file__), "static"),
		data_path=os.path.join(os.path.dirname(__file__),"data"),
		debug=torn.Debug(),
		cookie_secret = '35an18y3-u12u-7n10-4gf1-102g23ce04n6'
	)

application = Application(route, **settings)

if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(os.environ.get("PORT", 8000))
	IOLoop.current().start()

					
