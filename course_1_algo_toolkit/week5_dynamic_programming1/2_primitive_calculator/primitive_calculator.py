# Uses python3
import sys


def optimal_sequence(n):
    memeory_dict = {1: [0, -1], 2: [1, 1], 3: [1, 1]}
    sequence = []
    for i in range(4, n + 1):
        h_1, k_1 = memeory_dict[i-1]
        if i % 2 == 0 and i % 3 == 0:
            h_2, k_2 = memeory_dict[i // 2]
            h_3, k_3 = memeory_dict[i // 3]
            if h_1 <= h_2 and h_1 <= h_3:
                memeory_dict[i] = [h_1 + 1, i-1]
            elif h_2 <= h_3:
                memeory_dict[i] = [h_2 + 1, i // 2]
            else:
                memeory_dict[i] = [h_3 + 1, i // 3]
        elif i % 2 == 0:
            h_2, k_2 = memeory_dict[i // 2]
            if h_1 <= h_2:
                memeory_dict[i] = [h_1 + 1, i - 1]
            else:
                memeory_dict[i] = [h_2 + 1, i // 2]
        elif i % 3 == 0:
            h_3, k_3 = memeory_dict[i // 3]
            if h_1 <= h_3:
                memeory_dict[i] = [h_1 + 1, i - 1]
            else:
                memeory_dict[i] = [h_3 + 1, i // 3]
        else:
            memeory_dict[i] = [h_1 + 1, i - 1]
    sequence.append(n)
    curr = memeory_dict[n][1]
    while curr != -1:
        sequence.append(curr)
        curr = memeory_dict[curr][1]
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
