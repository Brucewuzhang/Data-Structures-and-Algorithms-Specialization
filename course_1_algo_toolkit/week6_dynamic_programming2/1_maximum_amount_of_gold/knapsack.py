# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    n = len(w)
    matrix = [[0] * (n+1) for _ in range(W + 1)]
    for i in range(W + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            else:
                matrix[i][j] = matrix[i][j-1]
                if w[j-1] <= i:
                    val = w[j-1] + matrix[i - w[j-1]][j-1]
                    if val > matrix[i][j]:
                        matrix[i][j] = val
    return matrix[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
