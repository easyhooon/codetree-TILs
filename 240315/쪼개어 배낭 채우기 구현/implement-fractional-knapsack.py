# 얻을 수 있는 최대 가치를 소수점 셋째짜리 까지 반올림
# 부동소수점 오차 있을거 같은데

import sys

si = sys.stdin.readline

n, m = map(int, si().split())
arr = []

for _ in range(n):
    w, v = map(int, si().split())
    arr.append((v / w, v, w))

arr.sort(reverse=True)
sum_v = 0
sum_w = 0

# print(a)

cnt = 0
while cnt < n:
    # 배열에 넣어서 저장 하면 메모리에러  M의 범위 고려해야한다...아닌데 10만인데 
    # 다 꺼내도 무게를 못채울수도 있구만 
    jewel = arr[cnt]
    # print(jewel[0], jewel[1], jewel[2])
    if sum_w + jewel[2] > m:
        sum_v += jewel[0] * (m - sum_w)
        break
    sum_v += jewel[1]
    sum_w += jewel[2]
    cnt += 1

print(f"{sum_v:.3f}")