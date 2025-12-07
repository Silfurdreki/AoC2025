import numpy as np

infile = "input.txt"
data = []
with open(infile) as input:
    for line in input:
        data.append(list(line)[:-1])

data = np.array(data)
numbers = []
results = []
for i in range(data.shape[1]-1, -1, -1):
    column = data[:,i]
    column_string = ''.join(column[:-1]).strip().rstrip()
    if not column_string:
        numbers = []
        continue
    operator = column[-1]
    numbers.append(int(column_string))
    if operator == "+":
        results.append(sum(numbers))
    elif operator == "*":
        results.append(int(np.prod(numbers)))
    
print(results)
print(sum(results))