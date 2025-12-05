infile = "input.txt"

with open(infile) as input:
    pos = 50
    zeros = 0
    for line in input:
        line = line.strip()
        sign = line[0]
        if len(line) == 2:
            n = int(line[-1])
        else:
            n = int(line[-2:])
        whole_rots = line[1:-2]
        if not whole_rots:
            rots = 0
        else:
            rots = int(whole_rots)
        if sign == "L":
            n = n * -1
        new_pos = pos + n
        rem = new_pos % 100

        if new_pos > 100:
            rots += 1
        elif new_pos < -100:
            rots += 1

        if new_pos < 0 and pos > 0:
            rots += 1

        if rem == 0:
            rots += 1

        zeros += rots
        print(pos, line, new_pos, rem, rots)
        pos = rem


print(zeros)
