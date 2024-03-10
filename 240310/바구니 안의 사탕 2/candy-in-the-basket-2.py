import sys

si = sys.stdin.readline

n, k = map(int, si().split())
temp_arr = []
max_coord = -sys.maxsize

#  단, 같은 위치에 여러 바구니가 놓여 있는 것이 가능함에 유의합니다.
for _ in range(n):
    cnt, coord = map(int, si().split())
    max_coord = max(max_coord, coord)
    temp_arr.append((coord, cnt))

arr = [0] * (max_coord + 1)

for coord, cnt in temp_arr:
    arr[coord] += cnt

max_sum = -sys.maxsize

for i in range(1, max_coord - 2 * k + 1):
    sum_val = 0
    for j in range(2 * k + 1):
        sum_val += arr[i + j]

    max_sum = max(max_sum, sum_val)

print(max_sum)