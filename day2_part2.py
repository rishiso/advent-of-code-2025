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

invalid = set()
for i in range(1, 99999): # Intervals contain at most 10 digits
    for j in range(2, 10):
        if len(str(i)) * j > 10:
            break

        combined = int(str(i) * j)
        if isInvalid(combined):
            invalid.add(combined)

print()
print(sum(invalid))