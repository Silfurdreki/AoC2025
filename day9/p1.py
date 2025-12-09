infile = "input.txt"

tiles = []
with open(infile) as input:
    for line in input:
        tiles.append([int(x) for x in line.strip().split(',')])

areas = []
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        areas.append(abs((tile1[0] - tile2[0] + 1) * (tile1[1] - tile2[1] + 1)))

print(sorted(areas)[-1])
