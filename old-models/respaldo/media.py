from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_pyfile('config.db.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:inxs0175@localhost/obras'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class MediaModel(db.Model):
	__tablename__ = 'media'
	#__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	media = db.Column('media', db.String(100))
	url = db.Column('url', db.Text)
	description = db.Column('descripction', db.Text)
	owner = db.Column('owner', db.Integer)
	ping = db.Column('ping', db.Integer)

