from flask_restful import reqparse,Resource
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help='this field is mandatory and will always be a float')
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help='every item needs to be assigned to a store')

    @jwt_required()
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "store not found"},404
        # return HTML status code 200 = OK if found item and 404 = Not found else.

    @jwt_required()
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message": "Store already exists"}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "an error occurred during item insertion"},500 # 500 - internal server error
        return store.json(), 201

    @jwt_required()
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            StoreModel.delete_from_db(store)
        return {"message": "Item deleted"}


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}