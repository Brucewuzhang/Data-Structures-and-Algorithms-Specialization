# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    remainder_sum_list = [0]
    previous = 0
    current = 1
    sum = 0

    period = -1
    for i in range(n):
        previous, current = current, (previous + current) % 10
        if previous == 0 and current == 1:
            period = i + 1
            break
        else:
            sum += previous * previous
            sum %= 10
            remainder_sum_list.append(sum)

    if period == -1:
        return sum
    return (remainder_sum_list[n % period] + remainder_sum_list[-1] * (n // period)) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
