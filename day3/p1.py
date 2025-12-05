infile = "input.txt"

def find_largest(row: list, start_i: int, end_i: int | None) -> tuple:
    highest = 9
    for highest in range(9, -1, -1):
        index = start_i
        for jolt in row[start_i:end_i]:
            if jolt == highest:
                return index, highest
            index += 1

banks_joltages = []
with open(infile) as input:
    for line in input:
        row = [int(x) for x in list(line.strip())]
        print(row)
        index, row_joltage_10 = find_largest(row, 0, -1)
        index, row_joltage_1 = find_largest(row, index+1, None)
        banks_joltages.append(row_joltage_10 * 10 + row_joltage_1)

print(banks_joltages)
print(sum(banks_joltages))
