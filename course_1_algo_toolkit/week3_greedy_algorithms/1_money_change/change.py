# Uses python3
import sys


def get_change(m):
    # write your code here
    n = 0
    for c in [10, 5, 1]:
        if m == 0:
            return n
        else:
            n += m // c
            m = m % c
    return n


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
