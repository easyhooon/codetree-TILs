import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))

max_sum = -sys.maxsize
sum_val = 0
last = 0
for i in range(n):
    sum_val = last + arr[i]
    if sum_val < 0:
        # 주어진 모든 수가 음수일 수 도 있음
        max_sum = max(max_sum, sum_val)
        last = 0
    else:
        last = sum_val 
        max_sum = max(max_sum, last)

print(max_sum)