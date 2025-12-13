import sys
import heapq
import math

lines = [i.strip() for i in sys.stdin.readlines()]
print()

n = len(lines)

graph = [[] for _ in range(n)]
nodes = []
for l in lines:
    nodes.append(tuple(int(i) for i in l.split(",")))

def distance(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += (p2[i] - p1[i]) ** 2
    
    return total

heap = []
for i in range(n):
    for j in range(i + 1, n):
        heap.append((distance(nodes[i], nodes[j]), i, j))

heapq.heapify(heap)

for _ in range(1000):
    _, i, j = heapq.heappop(heap)
    graph[i].append(j)
    graph[j].append(i)

seen = [False] * n

def dfs(i):
    if seen[i]:
        return 0
    
    seen[i] = True
    curr = 1
    for j in graph[i]:
        curr += dfs(j)
    
    return curr

circuits = []
for i in range(n):
    if not seen[i]:
        circuits.append(dfs(i))
        if len(circuits) > 3:
            circuits.remove(min(circuits))

print(math.prod(circuits))