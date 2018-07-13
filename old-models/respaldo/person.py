from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_pyfile('config.db.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:inxs0175@localhost/obras'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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

