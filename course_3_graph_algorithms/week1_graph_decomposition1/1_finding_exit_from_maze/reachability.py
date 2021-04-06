# Uses python3

import sys


def reach(adj, x, y, memory_dict={}):
    # write your code here
    if x in memory_dict:
        return 0
    memory_dict[x] = 1
    if x == y:
        return 1
    for v in adj[x]:
        if v in memory_dict:
            continue
        if reach(adj, v, y) == 1:
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    #     input = """4 2
    # 1 2
    # 3 2
    # 1 4"""
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
