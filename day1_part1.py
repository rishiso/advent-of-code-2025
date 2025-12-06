import sys
lines = sys.stdin.readlines()

cnt = 0
curr = 50
for turn in lines:
    mag = int(turn[1:])
    if turn[0] == 'L':
        mag *= -1
    
    curr = (curr + mag) % 100
    cnt += int(curr == 0)

print()
print(cnt)