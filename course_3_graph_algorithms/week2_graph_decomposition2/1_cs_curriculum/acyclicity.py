# Uses python3

import sys

post_count = 0


def dfs_post(g):
    global post_count
    post_count = 0
    post_order = {}
    visited = {}

    def explore(vertex):
        global post_count
        visited[vertex] = 1
        for v_ in g[vertex]:
            if v_ not in visited:
                explore(v_)
        post_order[vertex] = post_count
        post_count += 1

    for v in range(len(g)):
        if v not in visited:
            explore(v)
    return post_order


def acyclic(adj):
    # if acyclic, each strongly connected components can have at most 1 vertex
    adj_r = [[] for _ in range(n)]
    for i, edges_ in enumerate(adj):
        for j in edges_:
            adj_r[j].append(i)
    post_order = dfs_post(adj_r)
    v_p = list(post_order.items())
    v_p.sort(key=lambda x: x[1])
    visited = {}
    while v_p:
        sink = v_p[-1][0]
        visited[sink] = 1
        for v_ in adj[sink]:
            if v_ not in visited:
                return 1
        v_p.pop()
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """5 7
# 1 2
# 2 3
# 1 3
# 3 4
# 1 4
# 2 5
# 3 5"""
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
