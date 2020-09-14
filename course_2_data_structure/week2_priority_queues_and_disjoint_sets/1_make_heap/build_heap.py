# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    def shiftdown(i):
        min_index = i
        l_child_index = 2*i + 1
        r_child_index = 2*i + 2
        for index in [l_child_index, r_child_index]:
            if index <= n-1 and data[index] < data[min_index]:
                min_index = index
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append([i, min_index])
            shiftdown(min_index)
    swaps = []
    n = len(data)
    for i in range((n-2)//2, -1, -1):
        shiftdown(i)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
