from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def find(self, x):
        if self.parents[x] == x: return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.rank[x] > self.rank[y]: x, y = y, x
        self.parents[x] = y
        if self.rank[x] == self.rank[y]: self.rank[x] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

"""
uf = UnionFind(5)
print(uf)
uf.union(0, 4)
uf.union(0, 3)
print(uf)
uf.union(1, 2)
print(uf)
"""
