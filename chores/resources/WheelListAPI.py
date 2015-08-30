from flask import abort
from flask.ext.restful import Resource, reqparse

import chores.database as database


class WheelListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('people', type=list, location='json')
        self.reqparse.add_argument('chores', type=list, location='json')
        self.reqparse.add_argument('days_per_rotation', type=int, location='json')
        super(WheelListAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        try:
            new_id = database.new_wheel(args['people'], args['chores'], args['days_per_rotation'])
        except ValueError as e:
            print(e)
            if 'People and chores must be' in str(e):
                abort(500)
        return {'id': new_id}
