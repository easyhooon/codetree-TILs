import sys

si = sys.stdin.readline

def dfs(start):
    global cnt
    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            visited[i] = True
            dfs(i)

n, m = map(int, si().split())

cnt = 0

# 인접 리스트
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)

# 필수
visited[1] = True
dfs(1)

print(cnt)