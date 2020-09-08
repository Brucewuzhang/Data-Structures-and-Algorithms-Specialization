# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([next, i+1])
            continue

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            else:
                left, index = opening_brackets_stack.pop()
                if not are_matching(left, next):
                    return i + 1
                else:
                    continue
    if opening_brackets_stack:
        _, index = opening_brackets_stack.pop()
        return index
    else:
        return 0


def main():
    text = input()
    # text = '[]'
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
