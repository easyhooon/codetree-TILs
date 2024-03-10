import sys

si = sys.stdin.readline

n, m = map(int, si().split())

a_arr = list(map(int, si().split()))
b_arr = list(map(int, si().split()))

cnt = 0
for i in range(n - len(b_arr) + 1):
    temp_arr = []
    for j in range(i, i + len(b_arr)):
        temp_arr.append(a_arr[j])
    temp_arr.sort()
    b_arr.sort()
    if b_arr == temp_arr:
        cnt += 1

print(cnt)