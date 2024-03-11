import sys

si = sys.stdin.readline

arr = list(map(int, si().split()))
n = len(arr)
sum_arr = sum(arr)

min_diff = sys.maxsize
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a_sum = arr[i] + arr[j] + arr[k]
            min_diff = min(min_diff,  abs(a_sum - (sum_arr - a_sum)))

print(min_diff)