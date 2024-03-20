import sys

si = sys.stdin.readline

n = int(si())

num = [
    list(map(int, si().split()))
    for _ in range(n)
]

move_dir = [
    list(map(int, si().split()))
    for _ in range(n)
]

start_x, start_y = map(int, si().split())

answer = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, prev_num):
    return in_range(x, y) and num[x][y] > prev_num

def find_max(x, y, cnt):
    global answer
    answer = max(answer, cnt)

    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]

    d = move_dir[x][y] - 1

    for i in range(n):
        nx, ny = x + dxs[d] * i, y + dys[d] * i
        if can_go(nx, ny, num[x][y]):
            find_max(nx, ny, cnt + 1)

find_max(start_x - 1, start_y - 1, 0)
print(answer)