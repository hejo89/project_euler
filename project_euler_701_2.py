length = 4

import collections
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import time

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

#c = 0 
#for i in range(1, 2**(length**2)):
#    print(i)
#    tmp = bin(i)[2:]
#    arr = []
#    for j, k in enumerate(((length**2 - len(tmp)) * "0" + tmp)[::-1]):
#        if k == "1":
#            arr.append((j // length, j % length))
#    a = DisjSet(len(arr))
#    union(arr)
#    c += max_area(a.parent)



#print(round(float(c)/2**(length**2), 8))


####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################

def foo(a):

    a = zip(*a)

    # Your scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.scatter(a[0], a[1], color = 'red', s=10)

    # Add rectangles
    width = 1
    height = 1
    for a_x, a_y in zip(*a):
        ax.add_patch(Rectangle(
            xy=(a_x, a_y) ,width=width, height=height,
            linewidth=1, color='blue', fill=True))
    ax.axis('equal')


    for i in range(4):
        if i == 0 or i == 3:
            ax.axhline(y = i, linestyle='-', color='k', linewidth = 3) # horizontal lines
            ax.axvline(x = i, linestyle='-', color='k', linewidth = 3) # vertical lines

        else:
            ax.axhline(y = i, linestyle='--', color='k') # horizontal lines
            ax.axvline(x = i, linestyle='--', color='k') # vertical lines

    plt.show(block=False)

    plt.pause(0.5)

    plt.close()











####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################




s = []
for i in range(3):
    for j in range(3):
        s.append((i, j))





import itertools
for k in range(10):
    for j in itertools.combinations(s, k):
        foo(j)




















