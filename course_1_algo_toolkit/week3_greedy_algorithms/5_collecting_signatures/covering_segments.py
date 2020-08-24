# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key=lambda x: x[1])
    while len(segments) > 0:
        r_p = segments[0][1]
        points.append(r_p)
        for j in range(len(segments) - 1, -1, -1):
            if segments[j][0] <= r_p:
                segments.pop(j)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
