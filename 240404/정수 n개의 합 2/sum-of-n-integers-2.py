# 굳이 0번째에 값을 넣어주고 1 번째 입력부터 받지 말고
# 0번째를 예외처리의 형식으로 처리하자
import sys

si = sys.stdin.readline

n, k = map(int, si().split())
arr = list(map(int, si().split()))

ans = -sys.maxsize

ps = [0 for _ in range(n)]
for i in range(n):
    # 자기 자신은 항상 누적합에 포함됨
    ps[i] = arr[i]
    if i > 0:
        ps[i] += ps[i - 1]

# print(ps)

for i in range(n - k + 1):
    cnt = 0
    # a[i ... i+k-1] 의 합 구하기
    cnt = ps[i + k - 1]
    if i > 0:
        cnt -= ps[i - 1]
    ans = max(ans, cnt)

print(ans)