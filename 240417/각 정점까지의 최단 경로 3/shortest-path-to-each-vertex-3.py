# 다익스트라는 거리배열을 사용
# 거리배열을 INF 로 초기화하고 출발지의 값만 0으로 설정
# 이제 거리배열 내의 값들 최솟값을 골라주는데
# 이렇게 최솟값을 골라주는 과정을 다익스트라 알고리즘에서는 여러번 반복하므로
# 이런 경우에 효과적으로 최솟값을 계속 찾아주기 위해서는 우선순위 큐를 이용
# 따라서 처음 시작때부터 1번 부터 5번 정점까지 전부 우선순위 큐에 넣어 거리값 중 최솟값을 골라줌
# 시간 복잡도 O(ElogV)
# E: 간선의 수(선형 탐색), V: 정점의 수 (heappop() -> logN)

import heapq
import sys

INT_MAX = sys.maxsize

si = sys.stdin.readline


n, m = map(int, si().split())
start = 1

graph = [
    []
    for _ in range(n + 1)
]
pq = []

# 거리 배열
dist = [INT_MAX] * (n + 1)

for i in range(1, m + 1):
    x, y, z = map(int, si().split())
    graph[x].append((y, z))

dist[start] = 0
# (거리, 점) 으로 넣어서 거리가 작은 것이 먼저 나오도록 
heapq.heappush(pq, (0, start))

while pq:
    min_dist, min_index = heapq.heappop(pq)

    # 현재까지 계산한 최단 거리보다 더 크다면 (갱신이 이뤄지지 않음)
    if min_dist > dist[min_index]:
        continue

    # 이번에 뽑힌 점에 대해서 간선들을 검사 
    for target_index, target_dist in graph[min_index]:
        # 거리배열에서 현재까지 출발지점부터 뽑힌 점까지의 거리 + 거리 
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            # 거리 갱신 
            dist[target_index] = new_dist
            # 갱신 후 다시 pq 에 넣어주는 작업 수행 
            heapq.heappush(pq, (new_dist, target_index))

for i in range(2, n + 1):
    if dist[i] == INT_MAX:
        print(-1)
    else:
        print(dist[i])