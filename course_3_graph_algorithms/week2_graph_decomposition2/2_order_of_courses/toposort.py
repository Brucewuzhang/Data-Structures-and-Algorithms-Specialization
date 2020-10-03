# Uses python3

import sys

post_count = 0


def dfs(adj):
    # write your code here
    global post_count
    post_count = 0
    post_order = {}
    visisted = {}

    def explore(v):
        global post_count
        visisted[v] = 1
        for v_ in adj[v]:
            if v_ not in visisted:
                explore(v_)
        post_order[v] = post_count
        post_count += 1

    for v in range(len(adj)):
        if v not in visisted:
            explore(v)
    return post_order


def toposort(adj):
    used = [0] * len(adj)
    order = []
    # write your code here
    # sort using post-order
    post_order = dfs(adj)
    order = list(range(len(adj)))
    order.sort(key=lambda x: post_order[x], reverse=True)
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """5 7
# 2 1
# 3 2
# 3 1
# 4 3
# 4 1
# 5 2
# 5 3"""
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
