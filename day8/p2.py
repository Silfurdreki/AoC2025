import math
import numpy as np

infile = "input.txt"

def euclid_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2 + (coord1[2] - coord2[2])**2)

nodes = []
with open(infile) as input:
    for i, line in enumerate(input):
        nodes.append([int(x) for x in line.strip().split(",")])

distances = {}
for i, node1 in enumerate(nodes):
    for j, node2 in enumerate(nodes[i + 1:]):
        distance = euclid_distance(node1, node2)
        distances.update({distance: set([i, i + j + 1])})

sorted_distances = sorted(distances)
circuits = [distances[sorted_distances[0]]]
for distance in sorted_distances[1:]:
    circuit_match = 0
    for circuit in circuits:
        if distances[distance].intersection(circuit) and circuit_match == 0:
            circuit.update(distances[distance])
            matched_circuit = circuit
            circuit_match += 1
            continue
        elif distances[distance].intersection(circuit) and circuit_match > 0:
            circuit.update(matched_circuit)
            circuits.remove(matched_circuit)
            circuit_match += 1
            break
            
    if circuit_match < 1:
        circuits.append(distances[distance])
    if len(circuit) == len(nodes):
        last_boxes_locations = [nodes[x] for x in distances[distance]]
        break

final_prod = last_boxes_locations[0][0] * last_boxes_locations[1][0]
print(final_prod)