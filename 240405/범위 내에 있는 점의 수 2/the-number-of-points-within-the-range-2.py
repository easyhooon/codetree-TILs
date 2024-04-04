import sys

si = sys.stdin.readline

# query 를 미리 입력받아 pair의 형태로 저장 후에 가장 큰 값을 찾아 그 값으로 배열을 만들면 답 구할때 편할것같다
# 100만 40메가 바이트 가능한가 -> 시간초과

n, q = map(int, si().split())
a = list(map(int, si().split()))
query = []

MAX = 1000000
for _ in range(q):
    s, e = map(int, si().split())
    query.append((s, e))

ps = [0 for _ in range(MAX + 1)]

# preprocess
# s 입력으로 0이 들어올 수 있다.
for elem in a:
    ps[elem] = 1

# 이게 엄청 커질 수 있네
for i in range(1, MAX + 1):
    ps[i] += ps[i - 1]

for (s, e) in query:
    if s > 0:
        print(ps[e] - ps[s - 1])
    else:
        print(ps[e])