import sys 

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

max_area = -sys.maxsize


for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            # 3개의 점을 골랐을 때 각 변이 x, y 축에 평행하는지 검사 필요
            # x 축과 평행 -> y 좌표가 같다
            # y 축과 평행 -> x 좌표가 같다
            x_set = set()
            x_set.add(arr[i][0])
            x_set.add(arr[j][0])
            x_set.add(arr[k][0])
            y_set = set() 
            y_set.add(arr[i][1])
            y_set.add(arr[j][1])
            y_set.add(arr[k][1])
            if len(x_set) == 2 and len(y_set) == 2:
                max_area = max(max_area, arr[i][0] * arr[j][1] + arr[j][0] * arr[k][1] + arr[k][0] * arr[i][1] - arr[j][0] * arr[i][1] - arr[k][0] * arr[j][1] - arr[i][0] * arr[k][1])

print(max_area)