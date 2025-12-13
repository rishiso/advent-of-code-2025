import sys
import heapq

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

class UnionFind:
    
    def __init__(self, sz):
        self.parent = list(range(sz))
        self.components = sz

    def find(self, i):
        if self.parent[i] == i:
            return i
    
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if (root_a != root_b):
            self.parent[root_a] = root_b
            self.components -= 1

        return self.components == 1
    
uf = UnionFind(n)
heapq.heapify(heap)
while True:
    _, i, j = heapq.heappop(heap)
    if uf.union(i, j):
        print(nodes[i][0] * nodes[j][0])
        break

    
