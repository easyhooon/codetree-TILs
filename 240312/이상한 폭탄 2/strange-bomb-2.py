import sys

si = sys.stdin.readline

n, k = map(int, si().split())

arr = [
    int(si())
    for _ in range(n)
]

max_bomb_num = -sys.maxsize
for i in range(n - 1):
    for j in range(i + 1, min(n, i + k + 1)):
        if arr[i] == arr[j]:
            max_bomb_num = max(max_bomb_num, arr[i])

if max_bomb_num == -sys.maxsize:
    print(-1)
else:
    print(max_bomb_num)