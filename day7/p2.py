import re

def propagate_beam(beam_locs: dict, splitters: list) -> list:
    new_beam_locs = {}
    for beam_loc in beam_locs.keys():
        paths_to_here = beam_locs[beam_loc]
        if beam_loc in splitters:
            if beam_loc - 1 in new_beam_locs.keys():
                new_beam_locs[beam_loc - 1] = new_beam_locs[beam_loc - 1] + paths_to_here
            else:
                new_beam_locs.update({beam_loc - 1: paths_to_here})
            if beam_loc + 1 in new_beam_locs.keys():
                new_beam_locs[beam_loc + 1] = new_beam_locs[beam_loc + 1] + paths_to_here
            else:
                new_beam_locs.update({beam_loc + 1: paths_to_here})
        elif beam_loc in new_beam_locs.keys():
            new_beam_locs[beam_loc] = new_beam_locs[beam_loc] + paths_to_here
        else:
            new_beam_locs.update({beam_loc: paths_to_here})
    return new_beam_locs

infile = "input.txt"

splitters = []
with open(infile) as input:
    beam_locs = [input.readline().strip().find('S')]
    for line in input:
        row_spliters = [x.start() for x in re.finditer("\\^", line.strip())]
        if row_spliters:
            splitters.append(row_spliters)

beam_locs = dict(zip(beam_locs, [1]))
for splitter_row in splitters:
    beam_locs = propagate_beam(beam_locs, splitter_row)


print(sum(beam_locs.values()))