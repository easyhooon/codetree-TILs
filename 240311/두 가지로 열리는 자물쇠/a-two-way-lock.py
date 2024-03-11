import sys

si = sys.stdin.readline

n = int(si())

a, b, c = map(int, si().split())
a2, b2, c2 = map(int, si().split())

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            # if ~ else 로 카운트 하기 때문에 겹치는것 고려하지 않아도 됨 
            if (abs(a - i) <= 2 or abs(a - i) >= n - 2) and (abs(b - j) <= 2 or abs(b - j) >= n - 2) and \
               (abs(c - k) <= 2 or abs(c - k) >= n - 2):
                cnt += 1
			
            elif (abs(a2 - i) <= 2 or abs(a2 - i) >= n - 2) and (abs(b2 - j) <= 2 or abs(b2 - j) >= n - 2) and \
               (abs(c2 - k) <= 2 or abs(c2 - k) >= n - 2):
                cnt += 1

print(cnt)