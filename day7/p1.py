import re

def propagate_beam(beam_locs: list, splitters: list) -> list:
    splits = 0
    for i, beam_loc in enumerate(beam_locs):
        if beam_loc in splitters:
            beam_locs.pop(i)
            beam_locs.insert(i, beam_loc + 1)
            beam_locs.insert(i, beam_loc - 1)
            splits += 1
    return splits, list(set(beam_locs))

infile = "input.txt"

splitters = []
with open(infile) as input:
    beam_locs = [input.readline().strip().find('S')]
    for line in input:
        row_spliters = [x.start() for x in re.finditer("\\^", line.strip())]
        if row_spliters:
            splitters.append(row_spliters)

splits = 0
for splitter_row in splitters:
    new_splits, beam_locs = propagate_beam(beam_locs, splitter_row)
    splits += new_splits

print(beam_locs)
print(splits)