from flask_sqlalchemy import SQLAlchemy

#app.config.from_pyfile('config.db.cfg', silent=True)
user = 'user'
password = 'pass'
host = 'host'
port = 111111
database = 'db'
uri = "dribver://user:pass@host"

db = SQLAlchemy()



