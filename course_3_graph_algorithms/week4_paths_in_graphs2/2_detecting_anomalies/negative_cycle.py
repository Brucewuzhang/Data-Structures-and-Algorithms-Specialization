#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    # decompose it into parts
    D = {}
    for i in range(len(adj)):
        D[i] = float('inf')
    while D:
        s = list(D.keys())[0]
        D[s] = 0
        changed = False
        for i in range(len(D) - 1):
            for j in D:
                for l, k in enumerate(adj[j]):
                    if k not in D:
                        continue
                    cost_ = cost[j][l]
                    if cost_ + D[j] < D[k]:
                        D[k] = cost_ + D[j]
                        changed = True
            if not changed:
                break
        if changed:
            changed = False
            for j in D:
                for l, k in enumerate(adj[j]):
                    if k not in D:
                        continue
                    cost_ = cost[j][l]
                    if cost_ + D[j] < D[k]:
                        D[k] = cost_ + D[j]
                        changed = True
            if changed:
                return 1
        pop_list = []
        for k, v in D.items():
            if v == float('inf'):
                pop_list.append(k)
        for k in pop_list:
            D.pop(k)
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """4 4
# 1 2 -5
# 4 1 2
# 2 3 2
# 3 1 1"""
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
    print(negative_cycle(adj, cost))
