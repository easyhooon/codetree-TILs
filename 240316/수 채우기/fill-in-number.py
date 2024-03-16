import sys

si = sys.stdin.readline

n = int(si())

# cnt[0] = 5
# cnt[1] = 2

cnt = [0] * 2

while n >= 10:
    n -= 5
    cnt[0] += 1

if n % 5 % 2 == 0:
    cnt[0] += n // 5
    n %= 5
    cnt[1] += n // 2
    n %= 2
else:
    cnt[1] += n // 2
    n %= 2


if n != 0:
    print(-1)
else:
    print(sum(cnt))