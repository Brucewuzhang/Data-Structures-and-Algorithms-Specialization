# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    v_per_w = []
    for v, w in zip(values, weights):
        v_per_w.append(v / w)
    v_per_w_sorted = sorted(enumerate(v_per_w), key=lambda x: x[1], reverse=True)
    for i, vpw in v_per_w_sorted:
        if capacity == 0:
            return value
        a = min(capacity, weights[i])
        value += a * vpw
        capacity -= a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
