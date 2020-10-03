#Uses python3
import sys
import math

def minimum_distance(x, y):
    result = 0.
    #write your code here
    adj = [{} for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            dist = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            adj[i][j] = dist
            adj[j][i] = dist
    PrioQ = {}
    for i in range(len(x)):
        PrioQ[i] = float('inf')
    PrioQ[0] = 0
    while PrioQ:
        u = -1
        minimum = float('inf')
        for k, v in PrioQ.items():
            if v < minimum:
                minimum = v
                u = k
        result += minimum
        PrioQ.pop(u)
        for k, v in adj[u].items():
            if k in PrioQ and PrioQ[k] > adj[u][k]:
                PrioQ[k] = adj[u][k]
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """5
# 0 0
# 0 2
# 1 1
# 3 0
# 3 2"""
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
