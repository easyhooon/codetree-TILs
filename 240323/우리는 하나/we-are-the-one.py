import sys
from collections import deque

# k 개의 도시를 겹치지 않게 적절하게 골라, 골라진 k개의 도시로부터 갈 수 있는 서로 다른 도시의 수를 최대화

si = sys.stdin.readline

n, k, u, d = map(int, si().split())

grid = [
    list(map(int, si().split()))
    for _ in range(n)
]

s_pos = []
pos = []
for i in range(n):
    for j in range(n):
        pos.append((i, j))
q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]

answer = -sys.maxsize

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(cx, cy, nx, ny):
    return in_range(nx, ny) and not visited[nx][ny] and u <= abs(grid[cx][cy] - grid[nx][ny]) <= d

def bfs():
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dxs[i]
            ny = cy + dys[i]

            if can_go(cx, cy, nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

def calc():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    for x, y in s_pos:
        q.append((x, y))
        visited[x][y] = True 

    bfs()

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    return cnt


def find_max(curr_num, cnt):
    global answer
    if cnt > k:
        return 

    if curr_num == n * n:
        if cnt == k:
            answer = max(answer, calc())

        return

    s_pos.append(pos[curr_num])
    find_max(curr_num + 1, cnt + 1)
    s_pos.pop()

    find_max(curr_num + 1, cnt)

find_max(0, 0)

print(answer)