import sys
from collections import deque

si = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    global cnt
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dxs[i]
            ny = cy + dys[i]

            if in_range(nx, ny) and graph[nx][ny] != 1 and not check[nx][ny]:
                check[nx][ny] = True
                q.append((nx, ny))
                cnt += 1


n, k = map(int, si().split())

graph = [
    list(map(int, si().split()))
    for _ in range(n)
]

check = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
q = deque()

cnt = 0
for _ in range(k):
    x, y = map(int, si().split())
    q.append((x - 1, y - 1))
    check[x - 1][y - 1] = True
    cnt += 1

bfs()

print(cnt)