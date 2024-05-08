from flask import Flask
import requests as rq

from extentions import cache


class OpenStreetClient:

    def __init__(self):
        self.__root_url = "http://overpass-api.de/api/interpreter"
        self.__string_payload = """
        [out:json];
        (
            node["{0}"="{1}"]{2};
            way["{0}"="{1}"]{2};
            relation["{0}"="{1}"]{2};
        );
        out center;
        """
        self.__mapper = dict()

    def init_app(self, app: Flask):
        self.__mapper = app.config["OPEN_STREET_MAPPER"]

    @cache.memoize()
    def __find_element(self, element, area):
        if element not in self.__mapper:
            return None
        response = rq.get(self.__root_url, params={
            "data": self.__string_payload.format(self.__mapper[element], element, area)
        })
        data = response.json()
        return "elements" in data and len(data["elements"]) > 0

    @cache.memoize()
    def find_elements(self, elements, area):
        return {
            el: self.__find_element(el, area)
            for el in elements
        }
