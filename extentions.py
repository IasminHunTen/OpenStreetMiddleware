from flask_restx import Api
from flask_cors import CORS
from flask_caching import Cache

api = Api()
cors = CORS()
cache = Cache()

from services.open_street_client import OpenStreetClient

open_street_client = OpenStreetClient()
