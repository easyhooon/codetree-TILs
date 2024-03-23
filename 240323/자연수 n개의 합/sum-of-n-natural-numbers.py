import sys

si = sys.stdin.readline

s = int(si())

left = 1
right = s
max_num = 0

def is_possible(num):
    return num * (num + 1) // 2 <= s

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        answer = max(max_num, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)