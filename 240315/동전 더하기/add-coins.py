import sys

si = sys.stdin.readline

n, k = map(int, si().split())

arr = [
    int(si())
    for _ in range(n)
]

cnt = 0
for i in range(n - 1, -1, -1):
    if k % arr[i] == 0:
        cnt += k // arr[i]
        print(cnt)
        exit()
    else:
        cnt += k // arr[i]
        k %= arr[i]