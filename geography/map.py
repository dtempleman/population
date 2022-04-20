import geopandas as gpd
import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class Map():
    # points representing the outline of the landmass
    base: list = []
    # list points representing cities
    cities: list = []
    # set of provinces and associated meta data
    provinces: dict = dict()


def draw_map(map):
    # outputs a plot of the map data
    pass
