from flask import Flask,render_template
from flask_jwt import JWT
from flask_restful import Api
from resources.items import Item, ItemList
from resources.stores import Store, StoreList
from resources.index import index

from app_security import authenticate, identity
from resources.users import UserRegister

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" # db lives in the same folder as this code
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'buzi'
api = Api(app)

# JWT creates a new endpoint - '/auth', when we call it we send a username and password.
jwt = JWT(app,authentication_handler=authenticate,identity_handler=identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(index,'/')

# @app.route("/")
# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    db.create_all()
    app.run(port=5000, debug=True)
