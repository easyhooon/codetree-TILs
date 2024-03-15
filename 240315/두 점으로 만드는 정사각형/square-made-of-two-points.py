# 정사각형
import sys

si = sys.stdin.readline

x1, y1, x2, y2 = map(int, si().split())
a1, b1, a2, b2 = map(int, si().split())

max_x = max(x2, a2)
min_x = min(x1, a1)
max_y = max(y2, b2)
min_y = min(y1, b1)

x = max(max_x - min_x, max_y - min_y)

print(x * x)