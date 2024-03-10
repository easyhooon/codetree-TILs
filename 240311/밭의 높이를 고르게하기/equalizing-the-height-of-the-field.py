import sys

si = sys.stdin.readline

# 최소 t번 이상 h 높이로 나오게끔 
# 필요한 최소 비용 
# 연속하게!! 조건
# 차이가 적은 순으로 정렬하면 틀림 

'''
1 2 3 4 5 6 
3 번 이상 연속해서 3 높이
2 와 4를 3으로 만듬 -> 1 + 1 = 2
'''

n, h, t = map(int, si().split())
arr = list(map(int, si().split()))

diff_arr = [0] * n

for i in range(n):
    diff_arr[i] = abs(arr[i] - h)

# diff_arr.sort()

min_sum = sys.maxsize
for i in range(len(arr) -t + 1):
    temp_sum = 0
    for j in range(i, i + t):
        temp_sum += diff_arr[j]
    min_sum = min(min_sum, temp_sum)

print(min_sum)