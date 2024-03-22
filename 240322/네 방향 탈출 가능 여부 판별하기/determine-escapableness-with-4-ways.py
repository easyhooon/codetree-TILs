import sys
from collections import deque

si = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dxs[i]
            ny = cy + dys[i]

            if in_range(nx, ny) and grid[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


n, m = map(int, si().split())

grid = [
    list(map(int, si().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
q = deque()

bfs(0, 0)

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)