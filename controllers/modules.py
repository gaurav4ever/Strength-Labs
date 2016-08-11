
'''
Middleware for controller to contain all the modules
'''
import tornado.web, tornado.gen
import motor
from bson.objectid import ObjectId
import re

db = motor.MotorClient('mongodb://gaurav:dytila@ds027145.mlab.com:27145/dytila')['dytila']
					