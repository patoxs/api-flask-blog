from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_pyfile('config.db.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:inxs0175@localhost/obras'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

post_taxonomy = db.Table('post_taxonomy',
	db.Column('id_post', db.Integer, db.ForeignKey('post.id')),
	db.Column('id_taxonomy', db.Integer, db.ForeignKey('taxonomy.id'))
)

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
	key_activate = db.Column('key_activate', db.String(20))
	id_person_type = db.Column('id_person_type', db.Integer, db.ForeignKey('person_type.id'))

class MediaModel(db.Model):
	__tablename__ = 'media'
	#__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	media = db.Column('media', db.String(100))
	url = db.Column('url', db.Text)
	description = db.Column('descripction', db.Text)
	owner = db.Column('owner', db.Integer)
	ping = db.Column('ping', db.Integer)

class ConfigModel(db.Model):
	__tablename__ = 'config'
	#__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	param = db.Column('param', db.String(100))
	value = db.Column('value', db.Text)
	status = db.Column('status', db.Integer)
	type_config = db.Column('type_config', db.String(5))

class PostModel(db.Model):
	__tablename__ = 'post'
	#__table_args__ = {"schema":"araucaria"}
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
	id_post_taxonomy = db.relationship('PostModel', secondary=post_taxonomy, backref=db.backref('post_taxonomy', lazy='dynamic'))

class TaxonomyModel(db.Model):
	__tablename__ = 'taxonomy'
	#__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	taxonomy = db.Column('taxonomy', db.String(100))
	description = db.Column('description', db.Text)
	parent = db.Column('parent', db.Integer)
	status = db.Column('status', db.Integer)




