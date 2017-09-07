from flask_restful import reqparse,Resource
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='this field is mandatory and will always be a float')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='every item needs to be assigned to a store')

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "item not found"},404
        # return HTML status code 200 = OK if found item and 404 = Not found else.

    @jwt_required()
    def post(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return {"message": "Item already exists"}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name,data['price'],data["store_id"])
        try:
            item.save_to_db()
        except:
            return {"message": "an error occurred during item insertion"},500 # 500 - internal server error
        return item.json(), 201

    @jwt_required()
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            ItemModel.delete_from_db(item)
        return {"message": "Item deleted"}

    @jwt_required()
    def put(self,name):
        request_data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if not item:
            item = ItemModel(name,request_data["price"],request_data["store_id"])
        else:
            item.price = request_data["price"]
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}