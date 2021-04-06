# Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # write your code here
    distance[s] = 0
    changed = False
    for _ in range(len(distance) - 1):
        for u in range(len(distance)):
            for i, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][i]:
                    distance[v] = distance[u] + cost[u][i]
                    changed = True
        if not changed:
            break
    if not changed:
        for i, d in enumerate(distance):
            if d != float('inf'):
                reachable[i] = 1
    else:
        A = set()
        for u in range(len(distance)):
            for i, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][i]:
                    distance[v] = distance[u] + cost[u][i]
                    A.add(v)
        if len(A) == 0:
            for i, d in enumerate(distance):
                if d != float('inf'):
                    reachable[i] = 1
        else:
            visited = {}

            def bfs(v):
                visited[v] = True
                q = queue.Queue()
                q.put(v)
                while not q.empty():
                    curr_v = q.get()
                    for vi in adj[curr_v]:
                        if vi not in visited:
                            visited[vi] = True
                            q.put(vi)

            for v in A:
                if v not in visited:
                    bfs(v)
            for v in visited:
                shortest[v] = 0
            for i, d in enumerate(distance):
                if d != float('inf'):
                    reachable[i] = 1


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """5 4
# 1 2 1
# 4 1 2
# 2 3 2
# 3 1 -5
# 4"""
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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
