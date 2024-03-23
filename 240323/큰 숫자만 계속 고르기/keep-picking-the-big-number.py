import sys
import heapq

# 최대 힙
si = sys.stdin.readline

n, m = map(int, si().split())

pq = []
lst = list(map(int, si().split()))

for i in range(n):
    heapq.heappush(pq, -lst[i])

for i in range(m):
    max_val = -heapq.heappop(pq)
    max_val -= 1
    heapq.heappush(pq, -max_val)

print(-heapq.heappop(pq))