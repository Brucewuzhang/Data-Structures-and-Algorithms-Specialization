#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.aux_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.aux_stack:
            self.aux_stack.append(a)
        else:
            if a > self.aux_stack[-1]:
                self.aux_stack.append(a)
            else:
                self.aux_stack.append(self.aux_stack[-1])

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.aux_stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.aux_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
