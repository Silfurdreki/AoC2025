def check_repeated(id):
    id_str = str(id)
    if len(id_str) < 2:
        return False
    if id_str == len(id_str) * id_str[0] and len(id_str) < 3:
        return True
    if len(id_str) < 4:
        return False

    for div in range(2, (len(id_str) // 2) + 1):
        try:
            div_str = zip(*[iter(id_str)]*div, strict=True)
            divided_list = list(map(''.join, div_str))
        except ValueError:
            continue

        if len(set(divided_list)) <= 1 and len(divided_list) <= 2:
            return True

    return False

infile = "input.txt"

with open(infile) as input:
    indata = input.readline().strip()

inlist = indata.split(',')
repeat_ids = []
for id_range in inlist:
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])

    for id in range(start, end+1):
        if check_repeated(id):
            repeat_ids.append(id)

print(repeat_ids)
print(sum(repeat_ids))
