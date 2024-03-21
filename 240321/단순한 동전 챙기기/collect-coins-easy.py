import sys

si = sys.stdin.readline

n = int(si())

board = [
    list(si().strip())
    for _ in range(n)
]

# arr = []
# combination = []
answer = sys.maxsize

# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 'S':
#             arr.append((i, j))
#         if board[i][j] == 'E': 
#             arr.append((i, j))

# def calculate_dist():
#     global answer
#     coord = []
#     for elem in combination:
#         for i in range(n):
#             for j in range(n):
#                 if board[i][j] == str(elem):
#                     coord.append((i, j))
#     if len(coord) < 3:
#         return

#     # 이렇게 맨하탄 거리로 거리를 구하면 안됨 (가는길에 더 숫자가 큰 동전이 있을 수 있기 때문)
#     dist = abs(arr[0][0] - coord[0][0]) + abs(arr[0][1] - coord[0][1])
#     for i in range(1, len(coord)):
#         dist += abs(coord[i - 1][0] - coord[i][0]) + abs(coord[i - 1][1] - coord[i][1])

#     dist += abs(arr[1][0] - coord[len(coord) -1][0]) + abs(arr[1][1] - coord[len(coord) - 1][1])

#     answer = min(answer, dist)

# def choose(curr_num, cnt):
#     if curr_num == 10:
#         # 최소 동전 3개 
#         if cnt >= 3:
#             # print(combination)
#             calculate_dist()
#         return

#     combination.append(curr_num)
#     choose(curr_num + 1, cnt + 1)
#     combination.pop()

#     choose(curr_num + 1, cnt)

# choose(1, 0)

# if answer == sys.maxsize:
#     print('-1')
# else: 
#     print(answer)

COIN_NUM = 9
m = 3

coin_pos = []
selected_pos = []

start_pos = (-1, -1)
end_pos = (-1, -1)

def dist(a, b):
    (ax, ay), (bx, by) = a, b
    return abs(ax - bx) + abs(ay - by)

def calc():
    num_moves = dist(start_pos, selected_pos[0])
    for i in range(m - 1):
        num_moves += dist(selected_pos[i], selected_pos[i + 1])
    num_moves += dist(selected_pos[m - 1], end_pos)

    return num_moves

def find_min_moves(curr_idx, cnt):
    global answer

    if cnt == m:
        answer = min(answer, calc())
        return

    if curr_idx == len(coin_pos):
        return

    find_min_moves(curr_idx + 1, cnt)

    selected_pos.append(coin_pos[curr_idx])
    find_min_moves(curr_idx + 1, cnt + 1)
    selected_pos.pop()

for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            start_pos = (i, j)
        if board[i][j] == 'E':
            end_pos = (i, j)

for num in range(1, COIN_NUM + 1):
    for i in range(n):
        for j in range(n):
            if board[i][j] == str(num):
                coin_pos.append((i, j))

find_min_moves(0, 0)

if answer == sys.maxsize:
    answer = -1

print(answer)