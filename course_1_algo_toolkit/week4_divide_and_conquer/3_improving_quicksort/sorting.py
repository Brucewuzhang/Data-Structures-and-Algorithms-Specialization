# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    n = l
    m = 0
    for i in range(l+1, r+1):
        if a[i] < x:
            n += 1
            a[i], a[n] = a[n], a[i]
            if m > 0:
                a[n + m], a[i] = a[i], a[n + m]
        elif a[i] == x:
            m += 1
            a[n + m], a[i] = a[i], a[n + m]
    a[l], a[n] = a[n], a[l]
    return n, n + m




def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    n, m = partition3(a, l, r)
    randomized_quick_sort(a, l, n - 1)
    randomized_quick_sort(a, m + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n = 6
    # a = [33, 2, 33, 5, 33, 1]
    # # a = [6,5,4,3,2,1]
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
