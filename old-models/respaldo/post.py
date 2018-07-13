from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
#app.config.from_pyfile('config.db.cfg', silent=True)
user = 'pato'
password = 'inxs0175'
host = '144.217.240.227'
port = 5432
database = 'postgres'
uri = "postgresql://pato:inxs0175@144.217.240.227/postgres?client_encoding=utf8"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)


post_taxonomy = db.Table('araucaria.post_taxonomy',
	db.Column('id_post', db.Integer, db.ForeignKey('araucaria.post.id')),
	db.Column('id_taxonomy', db.Integer, db.ForeignKey('araucaria.taxonomy.id'))
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
	password = db.Column('password', db.String(20))
	url = db.Column('url', db.Text)
	modified = db.Column('modified', db.DateTime)
	parent = db.Column('parent', db.Integer)
	post_order = db.Column('post_order', db.Integer)
	id_person = db.Column('id_person', db.Integer)

	def __init__(self, title, excerpt, content, datetime, status, ping, password, url, modified, parent, post_order, id_person):
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

	def json(self):
		return {
			'title': self.title,
			'excerpt': self.excerpt,
			'content': self.content,
			'datetime': self.datetime,
			'status': self.status,
			'ping': self.ping,
			'password': self.password,
			'url': self.url,
			'modified': self.modified,
			'parent': self.parent,
			'post_order': self.post_order,
			'id_person': self.id_person
		}

	@classmethod
	def find_by_id(cls, id):
		return cls.query.filter_by(id = id).first()

	@classmethod
	def find_by_title(cls, title):
		return cls.query.filter_by(title = title).first()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()



class TaxonomyModel(db.Model):
	__tablename__ = 'taxonomy'
	__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	taxonomy = db.Column('taxonomy', db.String(100))
	description = db.Column('description', db.Text)
	parent = db.Column('parent', db.Integer)
	status = db.Column('status', db.Integer)

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


