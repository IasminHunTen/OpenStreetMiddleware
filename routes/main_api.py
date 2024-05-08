from flask_restx import Resource
from flask import request

from constants.models import RequestKeys
from extentions import api, open_street_client
from model.api_model import request_model
from model.marshmallow_schemas import RequestSchema

ns = api.namespace("flask-middleware")


@ns.route("/")
class MainResource(Resource):

    @ns.expect(request_model)
    @ns.param("ss", "square side in meters in which the search will be performed", default=500)
    def post(self):
        schema = RequestSchema()
        data = schema.load(ns.payload)
        square_side = int(request.args.get("ss", 500))
        return {
            RequestKeys.ELEMENTS: open_street_client.find_elements(
                schema.elements_set(data),
                schema.area(data, square_side)
            )
        }
