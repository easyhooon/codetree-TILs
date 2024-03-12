import sys

si = sys.stdin.readline

n, c, g ,h = map(int, si().split())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

max_sum = -sys.maxsize
for i in range(0, 1000):
    local_sum = 0
    for j in range(n):
        if i < arr[j][0]:
            local_sum += c

        elif arr[j][0] <= i <= arr[j][1]:
            local_sum += g

        else:
            local_sum += h

    max_sum = max(max_sum, local_sum)

print(max_sum)