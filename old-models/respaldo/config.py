from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_pyfile('config.db.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:inxs0175@localhost/obras'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ConfigModel(db.Model):
	__tablename__ = 'config'
	#__table_args__ = {"schema":"araucaria"}
	id = db.Column('id', db.Integer, primary_key=True)
	param = db.Column('param', db.String(100))
	value = db.Column('value', db.Text)
	status = db.Column('status', db.Integer)
	type_config = db.Column('type_config', db.String(5))


