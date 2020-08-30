# Uses python3
import sys
import itertools
import time


def partition3(A):
    if sum(A) % 3 != 0:
        return 0
    avg = sum(A) // 3
    for a in A:
        if a > avg:
            return 0
    A.sort()
    # t1 = time.time()
    pre_matrix = [[[0] * (avg + 1) for _ in range(avg + 1)] for _ in range(avg + 1)]
    curr_matrix = [[[0] * (avg + 1) for _ in range(avg + 1)] for _ in range(avg + 1)]
    # print(time.time() - t1)
    pre_matrix[0][0][0] = 1
    for i in range(1, len(A) + 1):
        a = A[i - 1]
        for j in range(a, avg + 1):
            for k in range(avg + 1):
                for l in range(k + 1):
                    if pre_matrix[j - a][k][l] == 1:
                        curr_matrix[j][k][l] = 1
                        curr_matrix[j][l][k] = 1
                        curr_matrix[k][j][l] = 1
                        curr_matrix[k][l][j] = 1
                        curr_matrix[l][k][j] = 1
                        curr_matrix[l][j][k] = 1
        pre_matrix = curr_matrix
        curr_matrix = [[[0] * (avg + 1) for _ in range(avg + 1)] for _ in range(avg + 1)]
    return pre_matrix[avg][avg][avg]


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """11
# 17 59 34 57 17 23 67 1 18 2 59"""
    n, *A = list(map(int, input.split()))
    print(partition3(A))
