
from controllers import *
route = [
		(
			r"/",
			home.homeHandler
		),
		(
			r"/bynow",
			home.bynowHandler
		),
		(
			r"/order",
			home.orderHandler
		)
]