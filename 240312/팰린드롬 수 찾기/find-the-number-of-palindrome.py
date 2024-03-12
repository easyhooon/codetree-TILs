import sys

si = sys.stdin.readline

x, y = map(int, si().split())

cnt = 0
for num in range(x, y + 1):
    # 홀수 짝수 나눌 필요가 없다 
    num = str(num)

    flag = True
    for i in range(len(num) // 2):
        if num[i] != num[-(i + 1)]:
            flag = False

    if flag:
        cnt += 1

print(cnt)