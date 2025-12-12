import numpy as np
import math

with open('day6.txt') as f:
    lines = [i.rstrip() for i in f.readlines()]

combined = []
mx_length = max(len(i) for i in lines[:-1]) + 1
for l in lines[:-1]:
    row = list(" " + l)
    row += (mx_length - len(row)) * [" "]
    combined.append(row)

combined = np.transpose(np.array(combined)).tolist()

sol = 0
ops = lines[-1].split()

for op in reversed(ops):
    nums = []

    while combined:
        n = "".join(combined.pop()).strip()
        if not n:
            break
        nums.append(int(n))

    if op == "+":
        sol += sum(nums)
    else:
        sol += math.prod(nums)

print(sol)
