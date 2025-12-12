import sys
from sortedcontainers import SortedList

lines = [i.strip() for i in sys.stdin.readlines()]
ranges = SortedList()
for line in lines:
    if not line:
        break
    
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

print()
print(sum(i[1] - i[0] + 1 for i in ranges))