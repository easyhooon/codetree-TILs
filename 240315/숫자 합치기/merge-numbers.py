import sys
import heapq 

si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
pq = []
for i in range(n):
    heapq.heappush(pq, arr[i])

# n이 10만이라 Loop 안에서 정렬을 수행하면 n^n log n 인데

min_sum = 0
# 두개씩 짝짓는거라 n - 1 번 (토너먼트))
for _ in range(n - 1):
    p1 = heapq.heappop(pq)
    p2 = heapq.heappop(pq)
    sum_val = p1 + p2
    min_sum += sum_val
    heapq.heappush(pq, sum_val)

print(min_sum)