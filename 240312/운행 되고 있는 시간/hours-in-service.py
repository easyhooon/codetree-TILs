import sys

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

max_start = 0
min_start = sys.maxsize
max_end = 0
min_end = sys.maxsize 

max_work_time = -sys.maxsize
for i in range(n):
    work_time = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        start = arr[j][0]
        end = arr[j][1]
        for k in range(start, end):
            work_time[k] = 1

    local_work_time = 0
    for l in range(1, 1001):
        if work_time[l] == 1:
            local_work_time += 1

    # print(local_work_time)
    max_work_time = max(max_work_time, local_work_time)

print(max_work_time)