import sys

si = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
R = -1

cnt = 0

sum_val = 0 
for L in range(n):
    while R + 1 < n and sum_val < m:
        R += 1
        sum_val += a[R]

    if sum_val == m:
        cnt += 1

    sum_val -= a[L]

print(cnt)