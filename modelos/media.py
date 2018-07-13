from flask import Flask
from db import db


class MediaModel(db.Model):
	__tablename__ = 'media'
	__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	media = db.Column('media', db.String(100))
	url = db.Column('url', db.Text)
	description = db.Column('description', db.Text)
	owner = db.Column('owner', db.Integer)
	ping = db.Column('ping', db.Integer)

	def __init__(self, media, url, description, owner, ping):
		self.media = media
		self.url = url
		self.description = description
		self.owner = owner
		self.ping = ping

	def json(self):
		return {
			'media': self.media,
			'url': self.url,
			'descripction': self.descripction,
			'owner': self.owner,
			'ping': self.ping
		}

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def return_all_post(cls, media, quantity):
		return cls.query.filter_by(media = media).limit(quantity)

