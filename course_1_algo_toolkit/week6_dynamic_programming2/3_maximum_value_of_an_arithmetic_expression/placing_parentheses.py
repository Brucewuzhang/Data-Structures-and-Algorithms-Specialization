# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    # write your code here
    digits = list(map(int, dataset[::2]))
    ops = dataset[1::2]
    m = [[0] * len(digits) for _ in range(len(digits))]
    M = [[0] * len(digits) for _ in range(len(digits))]
    for i in range(len(digits)):
        m[i][i] = digits[i]
        M[i][i] = digits[i]
    for i in range(1, len(digits)):
        for j in range(0, len(digits) - i):
            min_ = float('inf')
            max_ = -float('inf')
            for k in range(j, j + i):
                a = evalt(m[j][k], m[k + 1][j + i], ops[k])
                b = evalt(m[j][k], M[k + 1][j + i], ops[k])
                c = evalt(M[j][k], m[k + 1][j + i], ops[k])
                d = evalt(M[j][k], M[k + 1][j + i], ops[k])
                e = min(a, b, c, d)
                f = max(a, b, c, d)
                if min_ > e:
                    min_ = e
                if max_ < f:
                    max_ = f
            m[j][j + i] = min_
            M[j][j + i] = max_
    return M[0][len(digits) - 1]


if __name__ == "__main__":
    # print(get_maximum_value("5-8+7*4-8+9"))
    print(get_maximum_value(input()))
