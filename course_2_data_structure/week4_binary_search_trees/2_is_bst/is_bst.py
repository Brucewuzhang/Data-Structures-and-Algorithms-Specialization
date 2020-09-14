#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    n = len(tree)
    if n == 0:
        return True
    key = [0 for _ in range(n)]
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    max_ = [0 for _ in range(n)]
    min_ = [0 for _ in range(n)]
    for i in range(n):
        a, b, c = tree[i]
        key[i] = a
        left[i] = b
        right[i] = c

    s1 = [0]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if left[node] != -1:
            s1.append(left[node])
        if right[node] != -1:
            s1.append(right[node])
    while s2:
        node = s2.pop()
        if left[node] == -1 and right[node] == -1:
            max_[node] = key[node]
            min_[node] = key[node]
            continue
        if left[node] != -1:
            if max_[left[node]] > key[node]:
                return False
            else:
                max_[node] = key[node]
                min_[node] = min_[left[node]]
        else:
            max_[node] = key[node]
            min_[node] = key[node]

        if right[node] != -1:
            if min_[right[node]] < key[node]:
                return False
            else:
                max_[node] = max_[right[node]]
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
