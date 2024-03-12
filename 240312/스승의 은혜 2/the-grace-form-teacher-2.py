import sys

si = sys.stdin.readline

n, b = map(int, si().split())

arr = [
    int(si())
    for _ in range(n)
]

arr.sort()

sum_val = 0
cnt = 0
for i in range(n):
    if sum_val + arr[i] > b:
        if sum_val + arr[i] // 2 <= b:
            sum_val += arr[i] // 2
            cnt += 1
            break
        else:
            break
    sum_val += arr[i]
    cnt += 1

print(cnt)