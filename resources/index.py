from flask_restful import Resource
from flask import render_template,Response

class index(Resource):
    def get(self):
        return Response(render_template('index.html'),mimetype='text/html')