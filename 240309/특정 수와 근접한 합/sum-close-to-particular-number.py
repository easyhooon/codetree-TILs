import sys

si = sys.stdin.readline

def sum_arr(i, j):
    return sum(arr) - arr[i] - arr[j]

n, s = map(int, si().split())

arr = list(map(int, si().split()))

min_diff = sys.maxsize

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        min_diff = min(min_diff, abs(s - sum_arr(i, j)))

print(min_diff)