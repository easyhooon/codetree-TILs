# 두 자연수의 합이 가장 큰 쌍의 최솟값
import sys

si = sys.stdin.readline

n = int(si())

arr = []

cnt = 0

for _ in range(n):
    a, b = map(int, si().split())
    cnt += a
    for _ in range(a):
        arr.append(b)

arr.sort()

answer = -sys.maxsize
for i in range(cnt // 2):
    sum_val = arr[i] + arr[-(i + 1)]
    answer = max(answer, sum_val)

print(answer)