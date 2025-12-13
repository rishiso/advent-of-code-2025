import sys
from collections import deque

manifold = [i.strip() for i in sys.stdin.readlines()]
print()

rows = len(manifold)
cols = len(manifold[0])

q = deque()
seen = set()
for r in range(rows):
    for c in range(cols):
        if manifold[r][c] == 'S':
            q.append((r, c))
            seen.add((r, c))
            break

sol = 0
while q:
    sz = len(q)

    for _ in range(sz):
        seen.remove(q[0])

        r, c = q.popleft()
        r += 1

        if r < rows:
            if manifold[r][c] == '^':
                sol += 1
                if c - 1 >= 0 and (r, c - 1) not in seen:
                    q.append((r, c - 1))
                    seen.add((r, c - 1))

                if c + 1 < cols and (r, c + 1) not in seen:
                    q.append((r, c + 1))
                    seen.add((r, c + 1))
            
            elif (r, c) not in seen:
                q.append((r, c))
                seen.add((r, c))

print(sol)