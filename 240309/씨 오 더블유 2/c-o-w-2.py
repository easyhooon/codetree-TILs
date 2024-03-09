import sys

si = sys.stdin.readline

n = int(si())
arr = list(si())

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if arr[i] == 'C' and arr[j] == 'O' and arr[k] == 'W':
                cnt += 1

print(cnt)