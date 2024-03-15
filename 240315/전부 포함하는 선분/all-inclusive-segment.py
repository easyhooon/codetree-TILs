import sys

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

answer = sys.maxsize
for i in range(n):
    min_start = sys.maxsize
    max_end = -sys.maxsize
    for j in range(n):
        if i == j:
            continue
        
        min_start = min(min_start, arr[j][0])
        max_end = max(max_end, arr[j][1])

    answer = min(answer, max_end - min_start)

print(answer)