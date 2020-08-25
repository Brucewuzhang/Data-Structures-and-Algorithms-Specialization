# Uses python3

import sys


def IsGreaterOrEqual(digits, maxdigits):
    new_digits = digits + maxdigits
    new_max = maxdigits + digits
    return new_digits > new_max


def largest_number(a):
    # write your code here
    res = ""
    while len(a) > 0:
        maxdigits = a[0]
        max_index = 0
        for i, digits in enumerate(a[1:], start=1):
            if IsGreaterOrEqual(digits, maxdigits):
                maxdigits = digits
                max_index = i
        res += maxdigits
        a.pop(max_index)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
