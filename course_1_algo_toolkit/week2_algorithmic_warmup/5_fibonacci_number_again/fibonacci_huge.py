# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    remainder_list = [0]
    previous = 0
    current  = 1

    period = -1
    for i in range(n - 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            period = i + 1
            break
        else:
            remainder_list.append(previous)
    if period == -1:
        return current
    return remainder_list[n % period]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
