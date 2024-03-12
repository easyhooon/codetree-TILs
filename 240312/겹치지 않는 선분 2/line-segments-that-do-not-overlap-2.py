import sys

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

visited = [False] * 2000001

# 기울기가 더 급하면 교차한다.
# 시작점과 끝점 사이의 간격이 이전의 선분내에 포함되는 경우

# answer = n
# for i in range(n):
#     x1 = arr[i][0] + 1000000
#     x2 = arr[i][1] + 1000000

#     for j in range(x1, x2):
#         if visited[x1] and visited[x2]:
#             answer -= 2
#         visited[j] = True

# print(answer)

answer = 0

for i in range(n):
    overlap = False

    for j in range(n):
        if j == i:
            continue

        if (arr[i][0] <= arr[j][0] and arr[i][1] >= arr[j][1]) or (arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1]):
            overlap = True
            break

    if overlap == False:
        answer += 1

print(answer)