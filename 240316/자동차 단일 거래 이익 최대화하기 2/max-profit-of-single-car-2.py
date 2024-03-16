# n이 10만 이라 n^2으로 풀지 못함
# 차의 최댓값을 O(n)에 수행하는 방법 
import sys

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))

answer = 0

# 파는 날짜 기준으로 해당 날짜에 팔았을때 앞선 자동차 가격 중 최소를 골라주면 됨 -> N^2인데

# min_price = min(a)
# 갱신하는 방식으로
min_price = arr[0]

# 차이의 최댓값을 O(n)에 구현하는 방법 
for i in range(1, n):
    diff = arr[i] - min_price
    answer = max(answer, diff)

    min_price = min(min_price, arr[i])

print(answer)