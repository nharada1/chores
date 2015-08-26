from flask import abort
from flask.ext.restful import Resource, reqparse

import database


class WheelListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('people', type=list, location='json')
        self.reqparse.add_argument('chores', type=list, location='json')
        self.reqparse.add_argument('days_per_rotation', type=int, location='json')
        super(WheelListAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        new_id = database.new_wheel(args['people'], args['chores'], args['days_per_rotation'])
        return {'id': new_id}
