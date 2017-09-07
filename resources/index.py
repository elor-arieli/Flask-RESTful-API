from flask_restful import reqparse,Resource
from flask import render_template

class render_index(Resource):
    def get(self):
        return render_template('index.html')