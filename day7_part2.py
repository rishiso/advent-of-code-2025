import sys
from functools import cache

manifold = [i.strip() for i in sys.stdin.readlines()]
print()

rows = len(manifold)
cols = len(manifold[0])

@cache
def dfs(r, c):
    if r >= rows or c < 0 or c >= cols:
        return 1
    
    if manifold[r][c] == '^':
        return dfs(r, c + 1) + dfs(r, c - 1)

    return dfs(r + 1, c)

for r in range(rows):
    for c in range(cols):
        if manifold[r][c] == 'S':
            print(dfs(r, c))
            break