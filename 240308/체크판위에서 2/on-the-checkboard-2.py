import sys

si = sys.stdin.readline

r, c = map(int, si().split())

arr = [
    si().split()
    for _ in range(r)
]

cnt = 0
# 시작점과 종점 사이의 조건을 만족하는 두 정점의 쌍의 개수를 구하기 
for i in range(1, r - 1):
    for j in range(1, c - 1):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[r - 1][c - 1]:
                    cnt += 1

print(cnt)