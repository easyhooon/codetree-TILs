import sys
from collections import deque

si = sys.stdin.readline 

n, k = map(int, si().split())

q = deque()

for i in range(1, n + 1):
    q.append(i)

cnt = 0
while q:
    q.append(q.popleft())
    cnt += 1
    if cnt % k == 0:
        print(q.pop(), end=" ")