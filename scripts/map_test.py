from re import S
from geography.tile_map import SquareMap


height = 100
width = 100

map = SquareMap(width=width, height=height)


print(map)
for t in map.tiles:
    print(t)