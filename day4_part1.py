import sys

lines = [l.strip() for l in sys.stdin.readlines()]
print()

dirs = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1)
)

sol = 0
for r, row in enumerate(lines):
    for c, item in enumerate(row):
        if item == ".":
            continue

        cnt = 0
        for dr, dc in dirs:
            if r + dr >= 0 and r + dr < len(lines) and c + dc >= 0 and c + dc < len(row) and lines[r + dr][c + dc] == "@":
                cnt += 1
            
        sol += int(cnt < 4)

print(sol)