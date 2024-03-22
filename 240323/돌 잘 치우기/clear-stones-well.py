import sys
from collections import deque

si = sys.stdin.readline

# 백트래킹으로 m 개의 돌을 선택해서 치우고 k번 만큼 BFS 를 수행한 다음에
# 둘 중 최솟값을 산출하여 최솟값의 최댓값을 갱신
n, k, m = map(int, si().split())
grid = [
    list(map(int, si().split()))
    for _ in range(n)
]
visited  = [
    [False for _ in range(n)]
    for _ in range(n)
]
s_pos = []
stone = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stone.append((i, j))

selected_stones = []
q = deque()
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
answer = -sys.maxsize

for i in range(k):
    start_x, start_y = map(int, si().split())
    s_pos.append((start_x - 1, start_y - 1))

def find_max(curr_num, cnt):
    global answer
    if cnt > m:
        return

    if curr_num == len(stone):
        if cnt == m:
            answer = max(answer, calc())
        return

    selected_stones.append(stone[curr_num])
    find_max(curr_num + 1, cnt + 1)
    selected_stones.pop()

    find_max(curr_num + 1, cnt)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if in_range(nx, ny) and grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

def calc():
    for x, y in selected_stones:
        grid[x][y] = 0

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for x, y in s_pos:
        q.append((x, y))
        visited[x][y] = True

    bfs()   

    for elem in selected_stones:
        grid[elem[0]][elem[1]] = 1

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    return cnt

find_max(0, 0)

print(answer)