infile = "input.txt"

with open(infile) as input:
    pos = 50
    zeros = 0
    for line in input:
        line = line.strip()
        sign = line[0]
        n = int(line[1:])
        if sign == "L":
            n = n * -1

        pos = pos + n
        pos = pos % 100

        if pos == 0:
            zeros += 1

        print(pos)
print(zeros)
