import sys

si = sys.stdin.readline

arr = [
    list(map(int, si().split()))
    for _ in range(19)
]

# 가로 검사
for i in range(19):
    for j in range(15):
        if arr[i][j] == 1 and arr[i][j + 1] == 1 and arr[i][j + 2] == 1 and arr[i][j + 3] == 1 and arr[i][j + 4] == 1:
            print(1)
            print(i + 1, j + 3)

        if arr[i][j] == 2 and arr[i][j + 1] == 2 and arr[i][j + 2] == 2 and arr[i][j + 3] == 2 and arr[i][j + 4] == 2:
            print(2)
            print(i + 1, j + 3)
# 세로 검사
for i in range(15):
    for j in range(19):
        if arr[i][j] == 1 and arr[i + 1][j] == 1 and arr[i + 2][j] == 1 and arr[i + 3][j] == 1 and arr[i + 4][j] == 1:
            print(1)
            print(i + 3, j + 1)

        if arr[i][j] == 2 and arr[i + 1][j] == 2 and arr[i + 2][j] == 2 and arr[i + 3][j] == 2 and arr[i + 4][j] == 2:
            print(2)
            print(i + 3, j + 1)

# 대각선 검사(우하향)
for i in range(15):
    for j in range(15):
        if arr[i][j] == 1 and arr[i + 1][j + 1] == 1 and arr[i + 2][j + 2] == 1 and arr[i + 3][j + 3] == 1 and arr[i + 4][j + 4] == 1:
            print(1)
            print(i + 3, j + 3)

        if arr[i][j] == 2 and arr[i + 1][j + 1] == 2 and arr[i + 2][j + 2] == 2 and arr[i + 3][j + 3] == 2 and arr[i + 4][j + 4] == 2:
            print(2)
            print(i + 3, j + 3)

# 대각선 검사(우상향)
for i in range(5, 19):
    for j in range(15):
        if arr[i][j] == 1 and arr[i - 1][j + 1] == 1 and arr[i - 2][j + 2] == 1 and arr[i - 3][j + 3] == 1 and arr[i - 4][j + 4] == 1:
            print(1)
            print(i - 1, j + 3)

        if arr[i][j] == 2 and arr[i - 1][j + 1] == 2 and arr[i - 2][j + 2] == 2 and arr[i - 3][j - 3] == 2 and arr[i - 4][j + 4] == 2:
            print(2)
            print(i - 1, j + 3)