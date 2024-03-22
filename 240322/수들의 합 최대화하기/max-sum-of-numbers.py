import sys

si  = sys.stdin.readline

n = int(si())

board = [
    list(map(int, si().split()))
    for _ in range(n)
]

picked = []
visited = [False for _ in range(n)]

answer = -sys.maxsize

def find_max(curr_num):
    global answer
    if curr_num == n:
        answer = max(answer, sum(picked))

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            picked.append(board[curr_num][i])
            find_max(curr_num + 1)
            picked.pop()
            visited[i] = False


find_max(0)
print(answer)