from shapely.geometry import Polygon
from operator import attrgetter

class tile_pair():
    def __init__(self, tile1, tile2):
        self.tile1 = tile1
        self.tile2 = tile2
        self.area = (abs(tile1[0] - tile2[0]) + 1) * abs((tile1[1] - tile2[1]) + 1)

    def __repr__(self):
#        return repr(self.area)
        return repr((self.tile1, self.tile2))

infile = "input.txt"

with open(infile) as input:
    tiles = [[int(x) for x in input.readline().strip().split(',')]]
    for line in input:
        tiles.append([int(x) for x in line.strip().split(',')])

tile_polygon = Polygon(tiles)

tile_pairs = []
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        tile_pairs.append(tile_pair(tile1, tile2))

tile_pairs = sorted(tile_pairs, key=attrgetter("area"))
tile_pairs.reverse()

for i, tile_pair in enumerate(tile_pairs):
    other_corner1 = [tile_pair.tile1[0], tile_pair.tile2[1]]
    other_corner2 = [tile_pair.tile2[0], tile_pair.tile1[1]]
    square_polygon = Polygon([tile_pair.tile1, other_corner1, tile_pair.tile2, other_corner2])
    if tile_polygon.contains(square_polygon):
        largest_tile_pair = tile_pair
        break

print(largest_tile_pair.area)