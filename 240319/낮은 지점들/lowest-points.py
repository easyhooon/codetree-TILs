import sys
from collections import defaultdict

si = sys.stdin.readline

n = int(si())

d = defaultdict()

for i in range(n):
    x, y = map(int, si().split())
    if x not in d:
        d[x] = y
    else:
        cur_y = d[x]
        if y < cur_y:
            d[x] = y

answer = 0

for key, value in (d.items()):
    answer += value

print(answer)