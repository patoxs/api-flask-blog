from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from db import db

from security import authenticate, identity
from resources.post import PostResource, GetOnePostResource, GetListPostResource, GetSearchPostResource
from resources.person import PersonResource
from resources.media import MediaResource


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pato:inxs0175@144.217.240.227/postgres'
app.config.from_pyfile('config.cfg')

api = Api(app)
db.init_app(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(PostResource, '/post')
api.add_resource(GetOnePostResource, '/post/<int:year>/<int:month>/<string:title>')
api.add_resource(GetListPostResource, '/post_list/<string:taxonomy>/<int:quantity>')
api.add_resource(GetSearchPostResource, '/search/<string:word>')
api.add_resource(MediaResource, '/media')
api.add_resource(PersonResource, '/person/<string:email_author>')


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
