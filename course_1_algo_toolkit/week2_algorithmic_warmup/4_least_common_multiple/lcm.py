# Uses python3
import sys

def gcd_naive(a, b):
    if b == 0:
        return a
    else:
        a_ = a % b
    return gcd_naive(b, a_)

def lcm_naive(a, b):
    d = gcd_naive(a, b)
    a_ = a // d
    b_ = b //d

    return d * a_* b_

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

