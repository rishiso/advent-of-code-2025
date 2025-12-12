import numpy as np

with open('day6.txt') as f:
    lines = [i.strip() for i in f.readlines()]

combined = []
for l in lines[:-1]:
    combined.append(list(map(int, l.split())))

combined = np.array(combined)

sol = 0
ops = lines[-1].split()
for i in range(len(ops)):
    if ops[i] == "+":
        sol += combined[:, i].sum()
    else:
        sol += combined[:, i].prod()

print(sol)