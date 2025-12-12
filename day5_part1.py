import sys
from sortedcontainers import SortedList

line = sys.stdin.readline().strip()
ranges = SortedList()
while line:
    rng = [int(i) for i in line.split("-")]
    pos = ranges.bisect_left(tuple(rng))

    while pos < len(ranges) and ranges[pos][0] <= rng[1]:
        rng[1] = max(rng[1], ranges[pos][1])
        ranges.pop(pos)
    
    if pos - 1 >= 0 and ranges[pos - 1][1] >= rng[0]:
        rng[0] = ranges[pos - 1][0]
        rng[1] = max(rng[1], ranges[pos - 1][1])
        ranges.pop(pos - 1)

    ranges.add(tuple(rng))

    line = sys.stdin.readline().strip()

line = sys.stdin.readline().strip()
sol = 0
while line:
    id = int(line)
    pos = ranges.bisect_right((id, float('inf'))) - 1

    sol += int(pos >= 0 and id <= ranges[pos][1])
    line = sys.stdin.readline().strip()

print()
print(sol)