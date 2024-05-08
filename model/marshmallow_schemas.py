from marshmallow import Schema, fields, validate

from constants.models import RequestKeys
from utils.coordinates import calculate_deviation


class RequestSchema(Schema):
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    elements = fields.List(fields.String(required=True), validate=[validate.Length(min=1)])

    def area(self, data, delta):
        deviation = calculate_deviation(data[RequestKeys.LATITUDE], delta/2)
        return (
            data[RequestKeys.LATITUDE] - deviation.delta_latitude,
            data[RequestKeys.LONGITUDE] - deviation.delta_longitude,
            data[RequestKeys.LATITUDE] + deviation.delta_latitude,
            data[RequestKeys.LONGITUDE] + deviation.delta_longitude
        )

    def elements_set(self, data):
        return set(data[RequestKeys.ELEMENTS])
