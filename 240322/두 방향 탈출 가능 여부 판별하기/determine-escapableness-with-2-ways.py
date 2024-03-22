import sys

si = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y):
    global n, m
    if x == n - 1 and y == m - 1:
        return

    for i in range(2):
        nx = x + dxs[i]
        ny = y + dys[i]
        if in_range(nx, ny) and graph[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)


n, m = map(int, si().split())
graph = [
    list(map(int, si().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs, dys = [1, 0], [0, 1]

visited[0][0] = True
dfs(0, 0)

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)