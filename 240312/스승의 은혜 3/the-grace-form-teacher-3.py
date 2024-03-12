import sys

# 선물 하나를 정해서 반값으로 할인 받을 수 있다
# 선물 가능한 학생의 최대 '명수'를 출력 
# 배송비 추가 

si = sys.stdin.readline

# 1 <= n <= 1000, 1 <= b <= 1000
n, b = map(int, si().split())

p_arr, s_arr = [], []
for _ in range(n):
    # 1 <= p <= 1000, 1 <= s <= 1000
    p, s = map(int, si().split())
    p_arr.append(p)
    s_arr.append(s)

ans = 0
for i in range(n):
    tmp = [0] * n
    for j in range(n):
        tmp[j] = p_arr[j] + s_arr[j]
    tmp[i] = p_arr[i] // 2 + s_arr[i]

    tmp.sort()

    student = 0
    cnt = 0

    for j in range(n):
        if cnt + tmp[j] > b:
            break

        cnt += tmp[j]
        student += 1

    ans = max(ans, student)

print(ans)