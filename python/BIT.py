# Binary Indexed Tree(Fenwick Tree)
class BIT:
    def __init__(self, n=0):
        self.bit = [0] * (n + 1)
        self.len = n
    
    # 一点加算
    def add(self, index, x):
        i = index
        while i <= self.len:
            self.bit[i] += x
            i += i & -i
    
    # 区間[1, index]の和
    def sum(self, index):
        sm = 0
        i = index
        while i > 0:
            sm += self.bit[i]
            i -= i & -i
        return sm

    def __str__(self):
        return " ".join([str(self.sum(i) - self.sum(i-1)) for i in range(1, self.len+1)])

"""
bit = BIT(8)
bit.add(5, 3)
bit.add(4, -5)
print(bit.sum(8))
print(bit)
"""
