import json
import os

from flask import Flask

from extentions import api, cors, cache, open_street_client
from routes.main_api import ns


def create_app():
    app = Flask(__name__)
    with open("../config/default_config.json") as fd:
        app.config.update(json.load(fd))
    api.init_app(app)
    api.add_namespace(ns)
    cors.init_app(app)
    cache.init_app(app)
    open_street_client.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    if "DEVELOPMENT" in os.environ:
        app.run(debug=True)
    else:
        app.run("0.0.0.0")
