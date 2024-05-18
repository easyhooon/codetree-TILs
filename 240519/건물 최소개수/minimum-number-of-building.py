import sys

si = sys.stdin.readline 

n = int(si())

height = [0] * (n + 1)

for i in range(1, n + 1):
    x, y = map(int, si().split())
    height[i] = y

cnt = 0
stk = []

for i in range(1, n + 1):
    now = height[i]
    
    # 현재 높이보다 큰 높이가 스택에 있으면, 그 값을 제거하고 카운트합니다.
    while stk and stk[-1] > now:
        if stk[-1]:
            cnt += 1
        stk.pop()
        
    # 현재 높이와 같은 높이가 스택에 있으면, 그 값을 넘깁니다.
    if stk and stk[-1] == now:
        continue
    
    stk.append(now)

# 스택에 남아있는 값들을 카운트합니다.
while stk:
    if stk[-1]: 
        cnt += 1
    stk.pop()

# 결과를 출력합니다.
print(cnt)