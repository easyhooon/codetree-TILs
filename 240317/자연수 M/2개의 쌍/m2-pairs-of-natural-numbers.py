# 두 자연수의 합이 가장 큰 쌍의 최솟값
import sys

si = sys.stdin.readline

n = int(si())

arr = []

answer = 0

# for _ in range(n):
#     a, b = map(int, si().split())
#     cnt += a
#     for _ in range(a):
#         arr.append(b)

# arr.sort()

# answer = -sys.maxsize
# for i in range(cnt // 2):
#     sum_val = arr[i] + arr[-(i + 1)]
#     answer = max(answer, sum_val)

# print(answer)
    
nums = []
for _ in range(n):
    x, y = map(int, si().split())
    nums.append((y, x))

nums.sort()

li, ri = 0, n - 1

while li <= ri:
    ly, lx = nums[li]
    ry, rx = nums[ri]

    answer = max(answer, ly + ry)

    if lx < rx:
        nums[ri] = (ry, rx - lx)
        li += 1

    elif lx > rx:
        nums[li] = (ly, lx - rx)
        ri -= 1

    else:
        li += 1
        ri -= 1

print(answer)