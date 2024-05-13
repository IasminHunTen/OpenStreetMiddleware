from flask_restx import Resource
from flask import request
from geopy.distance import geodesic

from constants.models import RequestKeys
from extentions import api, open_street_client
from model.api_model import request_model
from model.marshmallow_schemas import RequestSchema

ns = api.namespace("flask-middleware")


@ns.route("/")
class MainResource(Resource):

    @ns.expect(request_model)
    @ns.param("ss", "square side in meters in which the search will be performed", default=250)
    def post(self):
        schema = RequestSchema()
        data = schema.load(ns.payload)
        square_side = int(request.args.get("ss", 250))
        elements = open_street_client.find_elements(
                schema.elements_set(data),
                schema.area(data, square_side)
        )
        return {
            RequestKeys.ELEMENTS: find_distance(
                origin=tuple([
                    data[RequestKeys.LATITUDE],
                    data[RequestKeys.LONGITUDE]
                ]),
                elements=elements
            )
        }


def find_distance(origin, elements):
    def for_one_element(value):
        if value is None:
            return None
        if not len(value):
            return -1.0
        return geodesic(origin, value).m
    return {
        k: for_one_element(v) for k, v in elements.items()
    }