# Uses python3
import sys

def fibonacci_sum_naive(n):
    # S_n+3 = 2 * S_n+2 - S_n
    if n <= 1:
        return n
    if n == 2:
        return 2

    S_b = 0  # S_i-2
    S_m = 1  # S_i-1
    S_c = 2  # S_i
    memory_dict = {(S_b, S_m, S_c): 0}
    remiander_list = [0]

    for i in range(n - 2):
        S_b, S_m, S_c = S_m, S_c, (2 * S_c - S_b) % 10
        if (S_b, S_m, S_c) in memory_dict:
            start_index = memory_dict[(S_b, S_m, S_c)]
            period = i - start_index + 1
            remiander_list = remiander_list[start_index:]
            return remiander_list[(n - start_index) % period]
        else:
            remiander_list.append(S_b)
            memory_dict[(S_b, S_m, S_c)] = i + 1

    return S_c

def fibonacci_partial_sum_naive(from_, to):
    if to < from_:
        return 0
    if from_ == 0:
        return fibonacci_sum_naive(to)
    return (fibonacci_sum_naive(to) - fibonacci_sum_naive(from_-1) + 10) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))