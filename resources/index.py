from flask_restful import reqparse,Resource
from flask import render_template

class render_index(Resource):
    def get(self):
        resp = make_response(render_template('index.html'))
        resp.mimetype = 'text/plain'
        return resp
        # return render_template('index.html')