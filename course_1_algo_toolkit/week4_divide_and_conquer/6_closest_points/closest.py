#Uses python3
import sys
import math

def minimum_distance(x, y):
    #write your code here
    if len(x) <= 1:
        return 10 ** 18
    if len(x) == 2:
        return ((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2) ** 0.5

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
