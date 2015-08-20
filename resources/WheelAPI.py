from flask import abort
from flask.ext.restful import Resource, reqparse

import database

from datetime import datetime
from dateutil.parser import parse


def rotate_list(list_in, n):
    """Rotate a list n values to the right

    Example:
        input:   [1,2,3,4,5,6], 2
        output:  [5,6,1,2,3,4]
    """
    x = n % len(list_in)
    return list_in[-x:] + list_in[:-x]


class WheelAPI(Resource):
    def __init__(self):
        super(WheelAPI, self).__init__()

    def get(self, id):
        result = database.get_wheel(id)
        if not result:
            abort(404)

        date_diff = datetime.now() - parse(result['date_created'])
        days_since = date_diff.days
        print(days_since)
        result['people'] = rotate_list(result['people'], days_since)
        result['chores'] = rotate_list(result['chores'], days_since)
        return result
