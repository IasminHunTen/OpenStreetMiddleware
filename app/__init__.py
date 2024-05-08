import json
import os
from pathlib import Path

from flask import Flask

from extentions import api, cors, cache, open_street_client
from routes.main_api import ns


def load_config():
    config_file = os.path.join(Path(__file__).parent.parent.absolute(), "config", "default_config.json")
    with open(config_file) as fd:
        return json.load(fd)


def create_app():
    app = Flask(__name__)
    app.config.update(load_config())
    api.init_app(app)
    api.add_namespace(ns)
    cors.init_app(app)
    cache.init_app(app)
    open_street_client.init_app(app)
    return app


app = create_app()

if __name__ == '__main__':
    if "DEVELOPMENT" in os.environ:
        app.run(debug=True)
    else:
        app.run("0.0.0.0")
