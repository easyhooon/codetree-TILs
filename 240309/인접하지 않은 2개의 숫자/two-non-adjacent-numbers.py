import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))

answer = -sys.maxsize

for i in range(n - 2):
    for j in range(i + 2, n):
        answer = max(answer, arr[i] + arr[j])

print(answer)