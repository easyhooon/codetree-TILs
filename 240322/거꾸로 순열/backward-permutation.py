import sys

si = sys.stdin.readline

n = int(si())

answer = [0] * (n + 1)
used = [False] * (n + 1)
    
def choose(curr_num):
    if curr_num == n + 1:
        for i in range(1, n + 1):
            print(answer[i], end=" ")
        print()
        return 
    
    for i in range(n, 0, -1):
        answer[curr_num] = i
        if used[i] is False:
            answer.append(i)
            used[i] = True
            choose(curr_num + 1)
            answer.pop()
            used[i] = False

choose(1)