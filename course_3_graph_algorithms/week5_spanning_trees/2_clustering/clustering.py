#Uses python3
import sys
import math


class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    # Finds set of given item x
    def find(self, x):

        # Finds the representative of the set
        # that x is an element of
        if (self.parent[x] != x):
            # if x is not the parent of itself
            # Then x is not the representative of
            # its set,
            self.parent[x] = self.find(self.parent[x])

            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set

        return self.parent[x]

    # Do union of two sets represented
    # by x and y.
    def Union(self, x, y):

        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

def clustering(x, y, k):
    #write your code here
    E = []
    dist = {}
    for i in range(len(x) - 1):
        for j in range(i+1, len(x)):
            dist[(i, j)] = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            E.append((i,j))
    n_clusters = len(x)
    disjset = DisjSet(len(x))
    E.sort(key=lambda x: dist[x])
    for (i, j) in E:
        if disjset.find(i) != disjset.find(j):
            if n_clusters == k:
                return dist[(i, j)]
            else:
                n_clusters -= 1
                disjset.Union(i, j)


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """8
# 3 1
# 1 2
# 4 6
# 9 8
# 9 9
# 8 9
# 3 11
# 4 12
# 4"""
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
