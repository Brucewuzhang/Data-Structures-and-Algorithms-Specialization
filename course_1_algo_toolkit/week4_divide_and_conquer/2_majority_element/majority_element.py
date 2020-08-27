# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    m = (right + left - 1) // 2
    l_major = get_majority_element(a, left, m + 1)
    r_major = get_majority_element(a, m + 1, right)
    if l_major == r_major:
        return l_major
    else:
        l_count = 0
        r_count = 0
        for i in a[left:right]:
            if i == l_major:
                l_count += 1
            elif i == r_major:
                r_count += 1
        l = right - left
        if l_count > l / 2:
            return l_major
        elif r_count > l / 2:
            return r_major
        else:
            return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n = 5
    # a = [2,3,9,2,2]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
