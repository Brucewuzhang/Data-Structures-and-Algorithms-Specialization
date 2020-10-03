# python3
import sys

NA = -1


class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = []


def build_trie(patterns):
    root = Node()
    for pattern in patterns:
        curr = root
        for c in pattern:
            found = False
            for node in curr.next:
                if node.value == c:
                    curr = node
                    found = True
                    break
            if not found:
                next_ = Node(c)
                curr.next.append(next_)
                curr = next_
    return root


def solve(text, n, patterns):
    result = []
    # write your code here
    trie = build_trie(patterns)
    for i in range(len(text)):
        curr = trie
        for j in range(i, len(text)):
            if not curr.next:
                break
            found = False
            for node in curr.next:
                if node.value == text[j]:
                    found = True
                    curr = node
                    break
            if not found:
                break
        if not curr.next:
            result.append(i)
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]
# text = "AATCGGGTTCAATCGGGGT"
# n= 0
# patterns = ['ATCG', 'GGGT']
ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
