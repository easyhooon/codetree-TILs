import sys
from collections import deque

si = sys.stdin.readline

n = int(si())
grid = [
    list(map(int, si().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

city_cnt = 0
people_cnt = 0
people_arr = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global people_cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_range(nx, ny) and grid[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            people_cnt += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            people_cnt = 1
            dfs(i, j)
            city_cnt += 1
            people_arr.append(people_cnt)

people_arr.sort()

print(city_cnt)

for i in range(len(people_arr)):
    print(people_arr[i])