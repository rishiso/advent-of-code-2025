import sys
lines = sys.stdin.readlines()
print()

cnt = 0
curr = 50
for turn in lines:
    mag = int(turn[1:])
    if turn[0] == 'L':
        mag *= -1
        if curr == 0:
            cnt -= 1

    curr += mag
    if curr > 0:
        cnt += curr // 100
    else:
        cnt += -(curr - 100) // 100

    curr = curr % 100

print(cnt)