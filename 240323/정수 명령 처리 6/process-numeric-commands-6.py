import sys
import heapq

# 최대 힙
si = sys.stdin.readline

n = int(si())

pq = []

for _ in range(n):
    cmd = si().strip()

    if cmd.startswith("push"):
        heapq.heappush(pq, -int(cmd.split()[1]))

    elif cmd.startswith("pop"):
        print(-heapq.heappop(pq))

    elif cmd.startswith("empty"):
        if not pq:
            print(1)
        else:
            print(0)
    elif cmd.startswith("top"):
        if not pq:
            print(0)
        else:
            print(-pq[0])
    
    elif cmd.startswith("size"):
        print(len(pq))