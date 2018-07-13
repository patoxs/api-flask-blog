from flask_sqlalchemy import SQLAlchemy

#app.config.from_pyfile('config.db.cfg', silent=True)
user = 'pato'
password = 'inxs0175'
host = '144.217.240.227'
port = 5432
database = 'postgres'
uri = "postgresql://pato:inxs0175@144.217.240.227/postgres?client_encoding=utf8"

db = SQLAlchemy()



