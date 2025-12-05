infile = "input.txt"

id_ranges = []
ingredients = []

with open(infile) as input:
    for line in input:
        if line == '\n':
            break
        else:
            tmp = (line.strip().split('-'))
            id_ranges.append([int(x) for x in tmp])

    for line in input:
        ingredients.append(int(line.strip()))

starts = [x[0] for x in id_ranges]
starts.sort()
ends = [x[1] for x in id_ranges]
ends.sort()

min_start = starts[0]
max_end = ends[0]
spoil_ranges = []
for var in zip(starts, ends):
    if var[0] > max_end + 1:
        spoil_ranges.append([max_end +1, var[0] - 1])
        min_start = var[0]
        max_end = var[1]
    if var[0] < min_start:
        min_start = var[0]
    if var[1] > max_end:
        max_end = var[1]

fresh = 0
for ingredient in ingredients:
    spoiled = False
    for spoil_range in spoil_ranges:
        if ingredient >= spoil_range[0] and ingredient <= spoil_range[1]:
            spoiled = True
            break
        elif ingredient < starts[0] or ingredient > ends[-1]:
            spoiled = True
            break
    if not spoiled:
        fresh += 1
print(fresh)
