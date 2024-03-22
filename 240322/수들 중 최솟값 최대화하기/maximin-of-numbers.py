import sys

si = sys.stdin.readline

n = int(si())

picked = []

graph = [[0] * (n + 1)]
for _ in range(n):
    graph.append([0] + list(map(int, si().split())))

visited = [
    [False for _ in range(n + 1)]
    for _ in range(n + 1)
]

answer = - sys.maxsize

def can_paint(r, c):
    flag = True
    
    # 같은 열에 색칠된 다른 칸이 있는지 체크
    for i in range(1, n + 1):
        if i != r and visited[i][c]:
            flag = False
            break

    return flag


# curr_num: 현재 색칠할 행
def find_max(curr_num):
    global answer
    # n 개의 칸을 모두 색칠 했을 때,
    if curr_num == n + 1:
        # 조건 2) 색칠된 칸에 적힌 수들 중 최솟값이 최대가 되도록
        min_num = min(picked)
        answer = max(answer, min_num)
        return 
    
    # 1 부터 n * n 번째 칸 중 하나를 선택하여 색칠
    for i in range(1, n + 1):
        # 배열에 들어간 수가 이미 min_num 보다 작다면 나머지를 볼 필요가 없다.
        if len(picked) > 0 and answer > min(picked):
           return

        # 조건 1) 각 행과 열을 정확히 1개만 색칠해야함
        if not can_paint(curr_num, i):
            continue
        
        visited[curr_num][i] = True
        # 색칠한 칸에 적힌 값 추가
        picked.append(graph[curr_num][i])
        # 다음 행으로 넘어감 
        find_max(curr_num + 1)
        picked.pop()
        visited[curr_num][i] = False
            

find_max(1)
print(answer)