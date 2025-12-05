import numpy as np

def check_removable(grid):
    removable_coords = []
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
                removable_coords.append((row, col))
    return removable_coords


infile = "input.txt"

grid = []
with open(infile) as input:
    for line in input:
        grid.append(list(line.strip()))

grid = np.array(grid)
removed = 0
rolls_to_remove = check_removable(grid)
while rolls_to_remove:
    for coords in rolls_to_remove:
        grid[coords] = "."
        removed += 1
    rolls_to_remove = check_removable(grid)

print(removed)
