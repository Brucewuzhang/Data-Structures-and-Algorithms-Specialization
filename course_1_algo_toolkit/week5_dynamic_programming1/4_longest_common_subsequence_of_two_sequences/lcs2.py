#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    n = len(a)
    m = len(b)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m+1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            else:
                if a[j -1] == b[i -1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    return matrix[m][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
