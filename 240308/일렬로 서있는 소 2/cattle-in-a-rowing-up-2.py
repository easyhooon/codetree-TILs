import sys

si = sys.stdin.readline

n = int(si())

height = list(map(int, si().split()))

cnt = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):

            if height[i] <= height[j] <= height[k]:
                cnt += 1

print(cnt)