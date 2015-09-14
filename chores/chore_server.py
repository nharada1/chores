from flask import Flask, make_response, jsonify
from flask.ext.restful import Api
from flask.ext.cors import CORS

from chores.resources import WheelAPI, WheelListAPI


def init_app():
    chore_app = Flask(__name__)
    CORS(chore_app)
    api = Api(chore_app)
    api.add_resource(WheelAPI, '/api/wheels/<string:id>', endpoint='wheel')
    api.add_resource(WheelListAPI, '/api/wheels', endpoint='wheels')
    return chore_app

chore_app = init_app()


@chore_app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def run_server():
    chore_app.run(debug=True)

if __name__ == "__main__":
    run_server()
