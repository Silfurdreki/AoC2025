import time

infile = "input.txt"

t0 = time.time()

def reduce_bank(row: list) -> int:
    bank = list(row)
    index = 0
    while len(bank) > 12:
        if bank[index] < bank[index + 1]:
            bank.pop(index)
            index = 0
        else:
            index += 1
        if index == len(bank) - 1:
            bank.pop(-1)
            index = 0
    return int(''.join([str(x)for x in bank]))

banks_joltages = []
with open(infile) as input:
    for line in input:
        row = [int(x) for x in list(line.strip())]
        reduced_row = reduce_bank(row)
        banks_joltages.append(reduced_row)

t = time.time() - t0

#print(banks_joltages)
print(sum(banks_joltages), t)


