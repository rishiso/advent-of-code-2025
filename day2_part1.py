import sys
import bisect

line = sys.stdin.read().strip()

intervals = []

for interval in line.split(","):
    intervals.append(tuple(int(i) for i in interval.split("-")))

intervals.sort()

def isInvalid(n):
    ind = bisect.bisect_right(intervals, (n, float('inf')))
    return ind - 1 >= 0 and n <= intervals[ind - 1][1]

sol = 0
for i in range(1, 99999): # Intervals contain at most 10 digits
    doubled = int(str(i) * 2)
    if isInvalid(doubled):
        sol += doubled

print()
print(sol)