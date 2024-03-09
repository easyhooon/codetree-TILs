import sys

si = sys.stdin.readline

n, k = map(int, si().split())

arr = [0] * 10001

for _ in range(n):
    x, y = map(str, si().split())
    x = int(x)
    if y == 'G':
        arr[x] = 1
    else:
        arr[x] = 2

max_sum = -sys.maxsize
for i in range(10001 - k):
    sum_val = arr[i]
    for j in range(1, k + 1):
        sum_val += arr[i + j]

    max_sum = max(max_sum, sum_val)

print(max_sum)