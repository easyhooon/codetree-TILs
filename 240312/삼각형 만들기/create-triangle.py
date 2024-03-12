import sys 

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

max_area = -sys.maxsize

for i in range(n):
    max_x = 0
    min_x = sys.maxsize
    max_y = 0
    min_y = sys.maxsize
    for j in range(n):
        if i == j:
            continue

        max_x = max(max_x, arr[j][0])
        min_x = min(min_x, arr[j][0])
        max_y = max(max_y, arr[j][1])
        min_y = min(min_y, arr[j][1])

    max_area = max(max_area, (max_x - min_x) * (max_y - min_y))

print(max_area)