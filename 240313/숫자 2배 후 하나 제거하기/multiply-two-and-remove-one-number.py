import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))

min_diff = sys.maxsize
for i in range(n):
    arr[i] *= 2
    
    for j in range(n):
        remaining_arr = []
        for k in range(n):
            if k != j:
                remaining_arr.append(arr[k])

        sum_diff = 0
        for k in range(n - 2):
            sum_diff += abs(remaining_arr[k + 1] - remaining_arr[k])

        min_diff = min(min_diff, sum_diff)

    arr[i] //= 2

print(min_diff)