# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    refills = 0
    current_p = 0
    n = len(stops)
    stops = [0] + stops + [distance]
    while current_p <= n:
        last_p = current_p
        x = stops[last_p]
        while current_p <= n and stops[current_p + 1] - x <= tank:
            current_p += 1
        if current_p == last_p:
            return -1
        if current_p <=n:
            refills += 1

    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
