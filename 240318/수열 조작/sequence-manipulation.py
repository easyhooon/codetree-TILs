import sys
from collections import deque

si = sys.stdin.readline

n = int(si())
q = deque()
for i in range(1, n + 1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])