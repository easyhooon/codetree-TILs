import sys

si = sys.stdin.readline

n = int(si())
a = list(map(int, si().split()))
b = list(map(int, si().split()))
c = list(map(int, si().split()))
d = list(map(int, si().split()))

count = dict()

cnt = 0

for i in range(n):
    for j in range(n):
        sum_val = a[i] + b[j]
        if sum_val in count:
            count[sum_val] += 1
        else:
            count[sum_val] = 1

for i in range(n):
    for j in range(n):
        diff = - c[i] - d[j]

        if diff in count:
            cnt += count[diff]


print(cnt)