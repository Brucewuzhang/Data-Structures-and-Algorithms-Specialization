# python3

import sys
import threading


def get_height_from_tree(tree, key):
    if key not in tree:
        return 0
    else:
        max_height = 0
        for child in tree[key]:
            height = get_height_from_tree(tree, child)
            if max_height < height:
                max_height = height
        return 1 + max_height


def compute_height(n, parents):
    # Replace this code with a faster implementation
    # max_height = 0
    children_dict = {}
    for vertex in range(n):
        parent = parents[vertex]
        if parent not in children_dict:
            children_dict[parent] = [vertex]
        else:
            children_dict[parent].append(vertex)
    max_height = get_height_from_tree(children_dict, -1)

    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
