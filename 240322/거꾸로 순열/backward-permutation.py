import sys

si = sys.stdin.readline

n = int(si())

picked = []
visited = [False] * (n + 1)
    
def choose(curr_num):
    if curr_num == n:
        for elem in picked:
            print(elem, end=" ")
        print()
        return 
    
    for i in range(n, 0, -1):
        if not visited[i]:
            picked.append(i)
            visited[i] = True
            choose(curr_num + 1)
            visited[i] = False
            picked.pop()
            
choose(0)