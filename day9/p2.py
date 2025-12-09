import numpy as np

infile = "test.txt"

with open(infile) as input:
    tiles = [[int(x) for x in input.readline().strip().split(',')]]
    for line in input:
        tiles.append([int(x) for x in line.strip().split(',')])

areas = {}
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        areas.update({abs((tile1[0] - tile2[0] + 1) * (tile1[1] - tile2[1] + 1)): [tile1, tile2]})

breakpoint()
