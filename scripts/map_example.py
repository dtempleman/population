import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import random

from shapely.geometry import Point


def random_points_in_polygon(number, polygon):
    points = []
    min_x, min_y, max_x, max_y = polygon.bounds
    i= 0
    while i < number:
        point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
        if polygon.contains(point):
            points.append(point)
            i += 1
    return points  # returns list of shapely point

gdf = gpd.read_file("data/map/canada/lpr_000b16a_e.shp")
fig, ax = plt.subplots(figsize=(12, 10))
gdf.plot(ax=ax, color="red")


# find the bounds of your geodataframe
x_min, y_min, x_max, y_max = gdf.total_bounds

# set sample size
n = 20
# generate random data within the bounds
x = np.random.uniform(x_min, x_max, n)
y = np.random.uniform(y_min, y_max, n)

# convert them to a points GeoSeries
gdf_points = gpd.GeoSeries(gpd.points_from_xy(x, y))
# only keep those points within polygons
gdf_points = gdf_points[gdf_points.within(gdf.unary_union)]
gdf_points.plot(ax=ax, color="black")


ax.axis("off")
plt.axis("equal")
plt.show()