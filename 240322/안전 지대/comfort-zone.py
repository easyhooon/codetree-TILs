import sys
sys.setrecursionlimit(10**4)

si = sys.stdin.readline

def progress():
    for i in range(n):
        for j in range(m):
            grid[i][j] -= 1

def initialize():
    global cnt
    cnt = 0

    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and grid[nx][ny] > 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

n, m = map(int, si().split())

grid = [
    list(map(int, si().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

max_k = -sys.maxsize

for i in range(n):
    k = max(grid[i])
    max_k = max(max_k, k)

max_count = -sys.maxsize
cnt = 0
answer = 0
for k in range(1, max_k + 1):
    progress()
    initialize()
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1

        if max_count < cnt:
            max_count = cnt
            answer = k

print(answer, max_count)