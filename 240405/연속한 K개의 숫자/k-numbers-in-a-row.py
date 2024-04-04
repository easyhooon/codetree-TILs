import sys

si = sys.stdin.readline

n, k, b = map(int, si().split())
arr = [0] * (n + 1)
prefix_sum = [0] * (n + 1)

def get_sum(s, e):
    return prefix_sum[e] - prefix_sum[s - 1]

answer = sys.maxsize

for _ in range(b):
    x = int(si())
    arr[x] = 1

prefix_sum[0] = 0
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for i in range(1, n - k + 2):
    answer = min(answer, get_sum(i, i + k - 1))

print(answer)