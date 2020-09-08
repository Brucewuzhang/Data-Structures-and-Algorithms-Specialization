# python3
from collections import deque


def max_sliding_window_naive(sequence, m):
    maximums = []
    Qi = deque()

    # Process first k (or first window)
    # elements of array
    for i in range(m):

        # For every element, the previous
        # smaller elements are useless
        # so remove them from Qi
        while Qi and sequence[i] >= sequence[Qi[-1]]:
            Qi.pop()

            # Add new element at rear of queue
        Qi.append(i)

        # Process rest of the elements, i.e.
    # from arr[k] to arr[n-1]
    for i in range(m, len(sequence)):

        # The element at the front of the
        # queue is the largest element of
        # previous window, so print it
        maximums.append(sequence[Qi[0]])

        # Remove the elements which are
        # out of this window
        while Qi and Qi[0] <= i - m:
            # remove from front of deque
            Qi.popleft()

            # Remove all elements smaller than
        # the currently being added element
        # (Remove useless elements)
        while Qi and sequence[i] >= sequence[Qi[-1]]:
            Qi.pop()

            # Add current element at the rear of Qi
        Qi.append(i)

        # Print the maximum element of last window
    maximums.append(sequence[Qi[0]])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

