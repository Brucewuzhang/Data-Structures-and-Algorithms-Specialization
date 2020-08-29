# Uses python3
import sys


def get_change(m):
    # write your code here
    if m <= 2:
        return m
    if m <= 4:
        return 1
    memory_list = [0] * (m + 1)
    memory_list[1], memory_list[2], memory_list[3], memory_list[4] = 1, 2, 1, 1
    for i in range(5, m+1):
        memory_list[i] = min(memory_list[i-1], memory_list[i-3], memory_list[i-4]) + 1
    return memory_list[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
