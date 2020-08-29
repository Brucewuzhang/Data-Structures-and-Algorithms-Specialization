# Uses python3
def edit_distance(s, t):
    # write your code here
    m = len(s)
    n = len(t)
    mat = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                mat[i][j] = j
            elif j == 0:
                mat[i][j] = i
            else:
                if s[i - 1] == t[j - 1]:
                    mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1])
                else:
                    mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1] + 1)
    return mat[m][n]


if __name__ == "__main__":
    # print(edit_distance('ab', 'ab'))
    print(edit_distance(input(), input()))
