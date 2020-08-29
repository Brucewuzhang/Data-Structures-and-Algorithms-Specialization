# Uses python3
import sys


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # write your code here
    pos = right - 1
    right_0 = ave
    right_1 = right
    left_1 = ave
    while right_0 - left > 0 and right_1 - left_1 > 0:
        if a[right_0 - 1] > a[right_1 - 1]:
            number_of_inversions += right_1 - left_1
            b[pos] = a[right_0 - 1]
            right_0 -= 1
        else:
            b[pos] = a[right_1 - 1]
            right_1 -= 1
        pos -= 1
    if right_0 - left > 0:
        for i in range(right_0 - 1, left - 1, -1):
            b[pos] = a[i]
            pos -= 1
    else:
        for i in range(right_1 - 1, left_1 - 1, -1):
            b[pos] = a[i]
            pos -= 1
    for i, v in enumerate(b[left: right], start=left):
        a[i] = v
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
#     input = """5
# 2 3 9 2 9"""
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
