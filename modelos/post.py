from flask import Flask
from db import db
from resources.jsonEncoder import DateTimeEncoder
from sqlalchemy import desc, asc
from sqlalchemy import func


post_taxonomy = db.Table('post_taxonomy',
	db.Column('id_post', db.Integer, db.ForeignKey('araucaria.post.id')),
	db.Column('id_taxonomy', db.Integer, db.ForeignKey('araucaria.taxonomy.id')),
	schema='araucaria'
)

class PostModel(db.Model):
	__tablename__ = 'post'
	__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	title = db.Column('title', db.Text)
	excerpt = db.Column('excerpt', db.Text)
	content = db.Column('content', db.Text)
	datetime = db.Column('datetime', db.DateTime)
	status = db.Column('status', db.Integer)
	ping = db.Column('ping', db.Integer)
	password = db.Column('password', db.String(80))
	url = db.Column('url', db.Text)
	modified = db.Column('modified', db.DateTime)
	parent = db.Column('parent', db.Integer)
	post_order = db.Column('post_order', db.Integer)
	id_person = db.Column('id_person', db.Integer)
	image = db.Column('image',  db.String(150))
	relaciones = db.relationship('TaxonomyModel', secondary=post_taxonomy, backref='relacionar')

	def __init__(self, title, excerpt, content, datetime, status, ping, password, url, modified, parent, post_order, id_person, image):
		self.title = title
		self.excerpt = excerpt
		self.content = content
		self.datetime = datetime
		self.status = status
		self.ping = ping
		self.password = password
		self.url = url
		self.modified = modified
		self.parent = parent
		self.post_order = post_order
		self.id_person = id_person
		self.image = image

	def json(self):
		return {
			'title': self.title,
			'excerpt': self.excerpt,
			'content': self.content,
			'datetime': DateTimeEncoder().encode(self.datetime.strftime("%d/%m/%Y")),
			'url': self.url,
			'id_person': self.id_person,
			'image':self.image
		}

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def create_relacion_taxonomy(cls,post,taxonomy):
		taxonomy.relacionar.append(post)
		db.session.commit()

	@classmethod
	def find_by_id(cls, id):
		return cls.query.filter_by(id = id).first()

	@classmethod
	def find_by_title(cls, title):
		return cls.query.filter_by(title = title).first()

	@classmethod
	def find_by_url(cls, url):
		return cls.query.filter_by(url = url).first()

	@classmethod
	def search_in_content(cls, word):
		word_search = '%' + word + '%'
		return cls.query.add_columns(
					PostModel.id,
					PostModel.title,
					PostModel.excerpt,
					PostModel.content,
					PostModel.datetime,
					PostModel.url,
					PostModel.image,
					TaxonomyModel.id,
					TaxonomyModel.taxonomy
				).join(
					post_taxonomy
				).join(
					TaxonomyModel
				).filter(
					PostModel.content.ilike(word_search)
				).order_by(
					PostModel.datetime.desc()
				).limit(20).all()

	@classmethod
	def return_all_post(cls, quantity):
		return cls.query.add_columns(
				PostModel.id,
				PostModel.title,
				PostModel.excerpt,
				PostModel.content,
				PostModel.datetime,
				PostModel.url,
				PostModel.image,
				TaxonomyModel.id,
				TaxonomyModel.taxonomy).join(post_taxonomy).join(TaxonomyModel).order_by(PostModel.datetime.desc()).limit(quantity).all()

	@classmethod
	def return_post_by_taxonomy(cls, taxonomy, quantity):
		return cls.query.add_columns(
				PostModel.id,
				PostModel.title,
				PostModel.excerpt,
				PostModel.content,
				PostModel.datetime,
				PostModel.url,
				PostModel.image,
				TaxonomyModel.id,
				TaxonomyModel.taxonomy).join(post_taxonomy).join(TaxonomyModel).filter(TaxonomyModel.taxonomy == taxonomy).order_by(PostModel.datetime.desc()).limit(quantity).all()



class TaxonomyModel(db.Model):
	__tablename__ = 'taxonomy'
	__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	taxonomy = db.Column('taxonomy', db.String(100))
	description = db.Column('description', db.Text)
	parent = db.Column('parent', db.Integer)
	status = db.Column('status', db.Integer)
	rel_taxonomy_post = db.relationship('PostModel', secondary=post_taxonomy, backref='relacionar_tax')

	def __init__(self, id, taxonomy, description, parent, status):
		self.id = id
		self.taxonomy = taxonomy
		self.description = description
		self.parent = parent
		self.status = status

	def json(self):
		return {
			'id': self.name,
			'taxonomy': self.taxonomy,
			'description': self.description,
			'parent': self.parent,
			'status': self.status
		}

	@classmethod
	def find_by_taxonomy(cls, taxonomy):
		return cls.query.filter_by(taxonomy = taxonomy).first()

	@classmethod
	def return_taxonomy(cls,news):
		return news.relacionar_tax

