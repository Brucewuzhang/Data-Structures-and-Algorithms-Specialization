# Uses python3
import sys


def optimal_summands(n):
    summands = []
    # write your code here
    # 1 + 2 + ... + k <= n < 1 + 2 + ... + k + k + 1
    # 0.5 * k * (K + 1) <=n < 0.5 * (k+1) * ( k + 2)
    if n == 0:
        return 0
    current_prize = 1
    summands.append(1)
    n -= current_prize
    current_prize += 1
    while n != 0:
        if n < current_prize:
            summands[-1] = summands[-1] + n
            return summands
        else:
            summands.append(current_prize)
            n -= current_prize
            current_prize += 1
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
