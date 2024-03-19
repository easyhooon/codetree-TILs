import sys
from collections import defaultdict

si = sys.stdin.readline

n, m = map(int, input().split())

d = defaultdict()

for i in range(1, n + 1):
    cmd = si().strip()
    d[cmd] = str(i)
    d[str(i)] = cmd

for i in range(m):
    cmd = si().strip()
    print(d[cmd])