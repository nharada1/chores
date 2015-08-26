#!flash/bin/python
from flask import Flask, make_response, jsonify
from flask.ext.restful import Api

from resources import WheelAPI, WheelListAPI

chores = Flask(__name__)
api = Api(chores)


@chores.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def run_server():
    api.add_resource(WheelAPI, '/api/wheels/<string:id>', endpoint='wheel')
    api.add_resource(WheelListAPI, '/api/wheels', endpoint='wheels')
    chores.run(debug=True)

if __name__ == "__main__":
    run_server()
