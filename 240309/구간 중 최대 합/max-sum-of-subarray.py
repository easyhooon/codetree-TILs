import sys

si = sys.stdin.readline

n, k = map(int, si().split())

arr = list(map(int, si().split()))

max_sum = -sys.maxsize

for i in range(n - k + 1):
    sum_val = arr[i]
    for j in range(1, k):
        sum_val += arr[i + j]
    max_sum = max(max_sum, sum_val)

print(max_sum)