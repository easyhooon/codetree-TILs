import sys

si = sys.stdin.readline

n = int(si())

arr = []
for _ in range(n):
    x, y = map(int, si().split())
    arr.append((x, y))

min_dist = sys.maxsize
for i in range(n - 1):
    for j in range(i + 1, n):
        min_dist = min(min_dist, (arr[i][0] - arr[j][0]) * (arr[i][0] - arr[j][0]) + (arr[i][1] - arr[j][1]) * (arr[i][1] - arr[j][1]))  

print(min_dist)