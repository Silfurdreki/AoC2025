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

starts = [x[0] for x in id_ranges]
starts.sort()
ends = [x[1] for x in id_ranges]
ends.sort()

min_start = starts[0]
max_end = ends[0]
spoil_intervals = []
for interval in zip(starts, ends):
    if interval[0] > max_end + 1:
        spoil_intervals.append([max_end +1, interval[0] - 1])
        min_start = interval[0]
        max_end = interval[1]
    if interval[0] < min_start:
        min_start = interval[0]
    if interval[1] > max_end:
        max_end = interval[1]

spoil_number = 0
for spoil_interval in spoil_intervals:
    spoil_number += spoil_interval[1] - spoil_interval[0] + 1

fresh = ends[-1] - starts[0] + 1 - spoil_number
print(fresh)
