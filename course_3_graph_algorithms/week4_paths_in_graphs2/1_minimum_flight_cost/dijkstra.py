#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    #write your code here
    # array implementation
    H = {}
    for i in range(len(adj)):
        H[i] = float('inf')
    H[s] = 0
    while H:
        u = -1
        minimum = float('inf')
        for i, v in H.items():
            if v < minimum:
                minimum = v
                u = i
        if u == -1:
            break
        elif u == t:
            return minimum
        H.pop(u)
        for i, v in enumerate(adj[u]):
            if v in H:
                cost_ = cost[u][i]
                if cost_ + minimum < H[v]:
                    H[v] = cost_ + minimum
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """3 3
# 1 2 7
# 1 3 5
# 2 3 2
# 3 2"""
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
