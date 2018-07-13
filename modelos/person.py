from flask import Flask
from db import db


class PersontypeModel(db.Model):
	__tablename__ = 'person_type'
	#__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	person_type = db.Column('person_type', db.String(100), unique=True)
	description = db.Column('descripction', db.String(255))
	id_person_type = db.relationship('PersonModel', backref='person_type', lazy='dynamic')


class PersonModel(db.Model):
	__tablename__ = 'person'
	__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	login = db.Column('login', db.String(50), unique=True)
	password = db.Column('password', db.String(30))
	nicename = db.Column('nicename', db.String(255))
	email = db.Column('email', db.String(100), unique=True)
	image = db.Column('image', db.String(300))
	status = db.Column('status', db.Integer)
	description = db.Column('description', db.String(500))
	facebook = db.Column('facebook', db.String(150))
	twitter = db.Column('twitter', db.String(150))
	key_activate = db.Column('key_activate', db.String(20))
	id_person_type = db.Column('id_person_type', db.Integer, db.ForeignKey('person_type.id'))

	def __init__(self, login, password, nicename, email,image, status, description, facebook, twitter, key_activate, id_person_type):
		self.login = login
		self.password = password
		self.nicename = nicename
		self.email = email
		self.image = image
		self.status = status
		self.descripction = descripction
		self.facebook = facebook
		self.twitter = twitter
		self.key_activate = key_activate
		self.id_person_type = id_person_type

	def json(self):
		return {
			'login': self.login,
			'nicename': self.nicename,
			'email': self.email,
			'image': self.image,
			'descripction': self.description,
			'facebook': self.facebook,
			'twitter':self.twitter
		}

	@classmethod
	def find_by_email(cls, email):
		return cls.query.filter_by(email = email).first()

	@classmethod
	def find_by_name(cls, username):
		return cls.query.filter_by(login = username).first()

	@classmethod
	def find_by_id(cls, id):
		return cls.query.filter_by(id = id).first()