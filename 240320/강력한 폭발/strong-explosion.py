import sys

si = sys.stdin.readline

n = int(si())

board = [
    list(map(int, si().split()))
    for _ in range(n)
]

bomb_cnt = 0

bomb_coord_arr = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bomb_cnt += 1
            bomb_coord_arr.append((i, j))

# 폭탄이 떨어질 위치에 어떤 폭탄을 넣을지 선택하여 최대 폭발 영역의 수 구하기

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

answer = -sys.maxsize
arr = []

def count_bomb_area():
    bomb_area_cnt = 0
    bomb_board = [[0] * n for _ in range(n)]
    for i in range(bomb_cnt):
        x, y = bomb_coord_arr[i]
        bomb_board[x][y] += 1
        if arr[i] == 1:
            for i in range(5):
                if in_range(x + i - 2, y):
                    bomb_board[x + i - 2][y] += 1

        elif arr[i] == 2:
            if in_range(x - 1, y):
                bomb_board[x - 1][y] += 1
            if in_range(x, y - 1):
                bomb_board[x][y - 1] += 1

            if in_range(x + 1, y):
                bomb_board[x + 1][y] += 1
            
            if in_range(x, y + 1):
                bomb_board[x][y + 1] += 1

        else:
            if in_range(x - 1, y - 1):
                bomb_board[x - 1][y - 1] += 1

            if in_range(x - 1, y + 1):
                bomb_board[x - 1][y + 1] += 1

            if in_range(x + 1, y - 1):
                bomb_board[x + 1][y - 1] += 1

            if in_range(x + 1, y + 1):
                bomb_board[x + 1][y + 1] += 1

    for i in range(n):
        for j in range(n):
            if bomb_board[i][j] >= 1:
                bomb_area_cnt += 1

    return bomb_area_cnt

def choose(curr_num):
    global answer
    if curr_num == bomb_cnt + 1:
        answer = max(answer, count_bomb_area())
        return 

    for i in range(1, 4):
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

choose(1)
print(answer)