#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs_post(adj):
    post_order = {}
    global post_count
    post_count = 0
    visited = {}

    def explore(v):
        global post_count
        visited[v] = 1
        for v_a in adj[v]:
            if v_a not in visited:
                explore(v_a)
        post_order[v] = post_count
        post_count += 1

    for v in range(len(adj)):
        if v not in visited:
            explore(v)

    return post_order


def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    adj_r = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            adj_r[j].append(i)
    post_order = dfs_post(adj_r)
    order = list(range(len(adj)))
    order.sort(key=lambda x: post_order[x], reverse=True)
    visited = {}

    def explore(v):
        visited[v] = True
        for v_a in adj[v]:
            if v_a not in visited:
                explore(v_a)

    for v in order:
        if v not in visited:
            result += 1
            explore(v)

    return result

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
    print(number_of_strongly_connected_components(adj))
