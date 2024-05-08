from flask_restx import fields

from extentions import api
from constants.models import RequestKeys

request_model = api.model("RequestModel", {
    RequestKeys.LATITUDE: fields.Float(required=True),
    RequestKeys.LONGITUDE: fields.Float(required=True),
    RequestKeys.ELEMENTS: fields.List(fields.String(required=True), min_items=1)
})
