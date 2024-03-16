import sys
import heapq

MAX_T = 10000

si = sys.stdin.readline

n = int(si())
bombs = []
for _ in range(n):
    score, time_limit = map(int, si().split())
    bombs.append((time_limit, score))

bombs.sort()

pq = []
bomb_idx = n - 1
ans = 0

for t in range(MAX_T, 0 , -1):
    # t초에 해체가 가능한 폭탄들을 전부 우선순위 큐에 담음
    while bomb_idx >= 0 and bombs[bomb_idx][0] == t:
        heapq.heappush(pq, -bombs[bomb_idx][1])
        bomb_idx -= 1

    # 현재 시간에 해체 가능한 폭탄이 존재한다면
    # 그 중 가장 높은 점수를 얻을 수 있는 폭탄을 해체 
    if pq:
        ans += -heapq.heappop(pq)

print(ans)