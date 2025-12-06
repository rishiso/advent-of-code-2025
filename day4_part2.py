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

rolls = set()
for r, row in enumerate(lines):
    for c, item in enumerate(row):
        if item == ".":
            continue
        
        rolls.add((r, c))

sol = 0
while rolls:
    removal = set()
    for r, c in rolls:
        cnt = 0
        for dr, dc in dirs:
            if (r + dr, c + dc) in rolls:
                cnt += 1
            
        if cnt < 4:
            removal.add((r, c))

    if not removal:
        break
    
    rolls = rolls.difference(removal)
    sol += len(removal)

print(sol)