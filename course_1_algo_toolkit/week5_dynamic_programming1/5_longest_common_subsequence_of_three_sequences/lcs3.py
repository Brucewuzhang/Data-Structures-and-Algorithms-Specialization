# Uses python3

import sys


def lcs3(a, b, c):
    # write your code here
    m = len(a)
    n = len(b)
    p = len(c)
    matrix = [[[0] * (p + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(p + 1):
                if i == 0 or j == 0 or k == 0:
                    matrix[i][j][k] = 0
                else:
                    if a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                        matrix[i][j][k] = matrix[i - 1][j - 1][k - 1] + 1
                    else:
                        matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1])
    return matrix[m][n][p]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
