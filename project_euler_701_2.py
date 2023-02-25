length = 5

import collections

class DisjSet:

    def __init__(self, n):

        self.parent = [i for i in range(n)]
 
 
    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
 
    def Union(self, x, y):
         
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)
 
        # If they are already in same set
        if xset == yset:
            return
 
        self.parent[xset] = yset

    def p(self):
        print(self.parent)



def max_area(us):
    d = collections.defaultdict(int)
    for j in us:
        d[a.find(j)] += 1
    return max(d.values())


def union(square):
    for i, j in enumerate(square[:-1]):
        for l, k in enumerate(square[i + 1:], i + 1):
            if (j[0] == k[0] and abs(j[1] - k[1]) == 1) or (j[1] == k[1] and abs(j[0] - k[0]) == 1):
                a.Union(i, l)

c = 0 
for i in range(1, 2**(length**2)):
    print(i)
    tmp = bin(i)[2:]
    arr = []
    for j, k in enumerate(((length**2 - len(tmp)) * "0" + tmp)[::-1]):
        if k == "1":
            arr.append((j // length, j % length))
    a = DisjSet(len(arr))
    union(arr)
    c += max_area(a.parent)



print(round(float(c)/2**(length**2), 8))
      

