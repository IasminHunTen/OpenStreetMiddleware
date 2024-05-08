from collections import namedtuple
from math import pi, cos

CoordinatesDeviation = namedtuple("CoordinatesDeviation", ["delta_latitude", "delta_longitude"])


def calculate_deviation(latitude, delta) -> CoordinatesDeviation:
    earth_radius = 6378.137 # in km
    dx = (1 / ((2 * pi / 360) * earth_radius)) / 1000 * delta
    dy = dx / cos(latitude * (pi / 180))
    return CoordinatesDeviation(dx, dy)
