# Uses python3
import sys


def x_less_n_left(starts, x):
    left = 0
    right = len(starts)
    while left < right:
        m = (left + right) // 2
        if starts[m] <= x:
            left = m + 1
        else:
            right = m - 1
    try:
        if starts[left] <= x:
            return len(starts) - left - 1
        else:
            return len(starts) - left
    except:
        return 0


def x_greater_n_right(ends, x):
    left = 0
    right = len(ends)
    while left < right:
        m = (left + right) // 2
        if ends[m] < x:
            left = m + 1
        else:
            right = m - 1
    try:
        if ends[left] < x:
            return left + 1
        else:
            return left
    except:
        return len(ends)


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    l_total = len(starts)
    # write your code here
    starts.sort()
    ends.sort()
    for i, x in enumerate(points):
        m = x_less_n_left(starts, x)
        n = x_greater_n_right(ends, x)
        cnt[i] = l_total - m - n
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """3 2
# 0 5
# -3 2
# 7 10
# 1 6"""
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
