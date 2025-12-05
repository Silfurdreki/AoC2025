import numpy as np

infile = "input.txt"

grid = []
with open(infile) as input:
    for line in input:
        grid.append(list(line.strip()))

grid = np.array(grid)
accessible = 0
for row in range(0, grid.shape[0]):
    for col in range(0, grid.shape[1]):
        if grid[row, col] == ".":
            continue
        around = grid[max(0, row - 1):min(grid.shape[0], row + 2), max(0, col - 1):min(grid.shape[1], col + 2)]
        if around.size < 4:
            continue
        unique, counts = np.unique(around, return_counts=True)
        amounts = dict(zip(unique, counts))
        if amounts["@"] - 1 < 4 and grid[row, col] == "@":
            accessible += 1

print(accessible)
