import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel as User

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',  #
                        type=str,
                        required=True,
                        help='this field is mandatory and will always be a string')
    parser.add_argument('password',  #
                        type=str,
                        required=True,
                        help='this field is mandatory and will always be a string')

    def post(self):
        data = UserRegister.parser.parse_args()
        user = User.find_by_username(data['username'])
        if user:
            return {"message": "A user with that username already exists"},400

        user = User(**data)
        user.save_to_db()
        return {"message": "user creted succesfully"},201