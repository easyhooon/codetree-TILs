import sys

si = sys.stdin.readline

n, m = map(int, si().split())

arr = [
    si().strip()
    for _ in range(n)
]

cnt = 0
# 가로 ->
for i in range(n):
    for j in range(m - 2):
        if arr[i][j] == 'L' and arr[i][j + 1] == 'E' and arr[i][j + 2] == 'E':
            cnt += 1

# 가로 <-
for i in range(n):
    for j in range(2, m):
        if arr[i][j] == 'L' and arr[i][j - 1] == 'E' and arr[i][j - 2] == 'E':
            cnt += 1

# 세로 아래
for i in range(n - 2):
    for j in range(m):
        if arr[i][j] == 'L' and arr[i + 1][j] == 'E' and arr[i + 2][j] == 'E':
            cnt += 1

# 세로 위
for i in range(2, n):
    for j in range(m):
        if arr[i][j] == 'L' and arr[i - 1][j] == 'E' and arr[i - 2][j] == 'E':
            cnt += 1

# 대각선 우상향
for i in range(2, n):
    for j in range(m - 2):
        if arr[i][j] == 'L' and arr[i - 1][j + 1] == 'E' and arr[i - 2][j + 2] == 'E':
            cnt += 1

# 대각선 우하향
for i in range(n - 2):
    for j in range(m - 2):
        if arr[i][j] == 'L' and arr[i + 1][j + 1] == 'E' and arr[i + 2][j + 2] == 'E':
            cnt += 1
    

# 대각선 좌상향
for i in range(2, n):
    for j in range(2, m):
        if arr[i][j] == 'L' and arr[i - 1][j - 1] == 'E' and arr[i - 2][j - 2] == 'E':
            cnt += 1

# 대각선 좌하향 
for i in range(n - 2):
    for j in range(2, m):
        if arr[i][j] == 'L' and arr[i + 1][j - 1] == 'E' and arr[i + 2][j - 2] == 'E':
            cnt += 1

print(cnt)