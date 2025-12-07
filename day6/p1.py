import re
import numpy as np

infile = "input.txt"
data = []
with open(infile) as input:
    for line in input:
        data.append(re.findall("[0-9+*]+", line.strip()))

operators = data.pop(-1)
data = np.array(data)
data = data.astype(int)

result = []
for col in range(0, data.shape[1]):
    if operators[col] == '+':
        result.append(sum(data[:,col]))
    elif operators[col] == '*':
        result.append(np.prod(data[:,col]))

print(result)
print(sum(result))