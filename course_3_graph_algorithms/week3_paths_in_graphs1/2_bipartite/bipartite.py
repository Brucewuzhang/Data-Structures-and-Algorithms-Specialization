#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    groups = [set() for _ in range(2)]
    visited = {}

    def bfs(v):
        # visited[v] = True
        q = queue.Queue()
        q.put(v)
        groups[0].add(v)
        while not q.empty():
            curr_v = q.get()
            if curr_v in groups[0]:
                curr_g = 0
            else:
                curr_g = 1
            visited[curr_v] = True
            for vi in adj[curr_v]:
                if vi not in visited:
                    visited[vi] = True
                    q.put(vi)
                    groups[1-curr_g].add(vi)
                else:
                    if vi not in groups[1-curr_g]:
                        return 0
        return 1
    for i in range(len(adj)):
        if i not in visited:
            flag = bfs(i)
            if not flag:
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """5 4
# 5 2
# 4 2
# 3 4
# 1 4"""
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
