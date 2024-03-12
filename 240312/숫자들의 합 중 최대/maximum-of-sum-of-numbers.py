import sys

si = sys.stdin.readline

x, y = map(int, si().split())

max_sum = -sys.maxsize
for i in range(x, y + 1):
    arr = list(str(i))
    local_sum = 0
    for elem in arr:
        local_sum += int(elem)
    max_sum = max(max_sum, local_sum)

print(max_sum)