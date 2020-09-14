# python3

import sys, threading, re

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []

        # Finish the implementation
        # You may need to add a new recursive method to do that
        current = 0
        stack = []
        while True:
            if current != -1:
                stack.append(current)
                current = self.left[current]
            elif stack:
                current = stack.pop()
                self.result.append(self.key[current])
                current = self.right[current]
            else:
                break

        return self.result

    def preOrder(self):
        self.result = []

        # Finish the implementation
        # You may need to add a new recursive method to do that
        stack = [0]
        while stack:
            current = stack.pop()
            self.result.append(self.key[current])
            if self.right[current] != -1:
                stack.append(self.right[current])
            if self.left[current] != -1:
                stack.append(self.left[current])

        return self.result

    def postOrder(self):
        self.result = []

        # Finish the implementation
        # You may need to add a new recursive method to do that
        # def postorder(i):
        #     if i == -1:
        #         return ""
        #     return str(postorder(self.left[i])) +" " + str(postorder(self.right[i])) + " " + str(self.key[i])
        # self.result = [s for s in re.split('\s+', postorder(0)) if s.strip() != '']
        # return self.result
        s1 = [0]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node)
            if self.left[node] != -1:
                s1.append(self.left[node])
            if self.right[node] != -1:
                s1.append(self.right[node])
        while s2:
            node = s2.pop()
            self.result.append(self.key[node])
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
