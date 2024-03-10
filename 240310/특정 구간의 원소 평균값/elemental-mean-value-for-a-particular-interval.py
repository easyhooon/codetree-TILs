import sys

si = sys.stdin.readline 

n = int(si())
arr = list(map(int, si().split()))

cnt = 0
for i in range(n):
    for j in range(i, n):
        temp_arr = arr[i:j + 1]
        temp_arr_average = sum(temp_arr) / len(temp_arr)
        if temp_arr_average in temp_arr:
            cnt += 1

print(cnt)