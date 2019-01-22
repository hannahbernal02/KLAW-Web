'''
	Contains classes necessary for User.

	Author: Chris Carrillo
	Date: 1/12/2019
'''

from marshmallow import Schema, fields
from sqlalchemy import Column, String, Text
from sqlalchemy_utils import UUIDType
from flask_login import UserMixin

from .database import Base

import uuid

class User(Base, UserMixin):
	'''
		The User class defines the user object that will be inserted into the database.
		A User has a user_id, an email, a first_name, a last_name, and a password.
	'''

	__tablename__ = "USER"

	# binary=False falls back to CHAR instead of BINARY
	user_id = Column(UUIDType(binary=True), primary_key = True)
	email = Column(String, unique=True, nullable = False)
	first_name = Column(String, nullable = False)
	last_name = Column(String, nullable = False)
	password = Column(Text, nullable = False)

	def __init__(self, user_id, email, first_name, last_name, password):
		self.user_id = user_id
		self.email = email
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

class UserSchema(Schema):
	'''
		UserSchema is used to transform instances of User into JSON objects.
	'''

	user_id = fields.UUID()
	email = fields.Str()
	first_name = fields.Str()
	last_name = fields.Str()
	password = fields.Str()