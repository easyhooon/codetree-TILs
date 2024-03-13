import sys

si = sys.stdin.readline 

a, b, c = map(int, si().split())

a_max_cnt = c // a
b_max_cnt = c // b

max_sum = -sys.maxsize
for i in range(1, a_max_cnt + 1):
    for j in range(1, b_max_cnt + 1):
        if a * i + b * j >= c:
            break

        max_sum = max(max_sum, a * i + b * j)

print(max_sum)