import sys
from collections import deque

si = sys.stdin.readline

def in_range(x, y):
    return 0 < x <= n and 0 < y <= n

def can_go(nx, ny):
    return in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] < grid[start_x][start_y]

def initialize():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            visited[i][j] = False

def bfs(x, y):
    global start_x, start_y, max_val, best_x, best_y
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    # q에 들어오는 것이 없으면 사방이 막힌것 start_x, start_y 갱신안됨
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dxs[i]
            ny = cy + dys[i]

            # 이동은 가능할때까지 하는데 최댓값(최적위치는)은 갱신되도록
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                if grid[nx][ny] >= max_val:
                    if grid[nx][ny] == max_val:
                        if best_x >= nx:
                            if best_x == nx:
                                if best_y >= ny:
                                    best_y = ny
                            else:
                                best_x = nx
                                best_y = ny

                    else:
                        max_val = grid[nx][ny]
                        best_x = nx
                        best_y = ny


n, k = map(int, si().split())

grid = [[0] * (n + 1)]
for _ in range(n):
    grid.append([0] + list(map(int, si().split())))

visited = [
    [False] * (n + 1)
    for _ in range(n + 1)
]

start_x, start_y = map(int, si().split())

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

max_val = -sys.maxsize
best_x = start_x
best_y = start_y

cnt = 0

while cnt < k:
    max_val = -sys.maxsize
    initialize()
    bfs(start_x, start_y)
    start_x = best_x
    start_y = best_y
    cnt += 1

print(start_x, start_y)