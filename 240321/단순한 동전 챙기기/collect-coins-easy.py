import sys

si = sys.stdin.readline

n = int(si())

board = [
    list(si().strip())
    for _ in range(n)
]

arr = []
combination = []
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            arr.append((i, j))
        if board[i][j] == 'E': 
            arr.append((i, j))

def calculate_dist():
    global answer
    coord = []
    for elem in combination:
        for i in range(n):
            for j in range(n):
                if board[i][j] == str(elem):
                    coord.append((i, j))
    if len(coord) < 3:
        return

    dist = abs(arr[0][0] - coord[0][0]) + abs(arr[0][1] - coord[0][1])
    for i in range(1, len(coord)):
        dist += abs(coord[i - 1][0] - coord[i][0]) + abs(coord[i - 1][1] - coord[i][1])

    dist += abs(arr[1][0] - coord[len(coord) -1][0]) + abs(arr[1][1] - coord[len(coord) - 1][1])

    answer = min(answer, dist)

def choose(curr_num, cnt):
    if curr_num == 10:
        # 최소 동전 3개 
        if cnt >= 3:
            # print(combination)
            calculate_dist()
        return

    combination.append(curr_num)
    choose(curr_num + 1, cnt + 1)
    combination.pop()

    choose(curr_num + 1, cnt)

choose(1, 0)

if answer == sys.maxsize:
    print('-1')
else: 
    print(answer)