from dataclasses import dataclass
from enum import Enum, auto
from typing import List


class MapType(Enum):
    SQUARE = auto()


@dataclass
class Tile():
    loc: List[int] = List
    
    def __init__(self, x: int, y: int):
        self.loc = [x, y]

    def __str__(self):
        return f"Tile at ({self.loc[0]}, {self.loc[1]})"


@dataclass
class SquareTile(Tile):
    pass


@dataclass
class TileMap():
    dim: List[int] = List
    tiles: List[Tile] = List

    def __init__(self, width: int, height: int):
        self.dim = [width, height]

    def add_tile(self, tile: Tile):
        self.tiles.append(tile)


@dataclass
class SquareMap(TileMap):

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.generate_map()

    def generate_map(self):
        for w in range(self.dim[0]):
            for h in range(self.dim[1]):
                self.add_tile(Tile(w, h))

    def __str__(self):
        return f"Square map with dimentions {self.dim[0]}/{self.dim[1]}"