import sys

si = sys.stdin.readline

n = int(si())

arr = [
    int(si())
    for _ in range(n)
]

sorted_arr = sorted(arr)
start = sorted_arr[0]
end = sorted_arr[len(sorted_arr) - 1]

max_cnt = -sys.maxsize
for i in range(1, end + 1):
    cnt = 0
    flag = False # 해수면의 높이보다 arr[j]가 높으면 True 낮으면 False
    for j in range(n):
        if arr[j] > i:
            if not flag:
                cnt += 1
                flag = True

        else:
            if flag:
                flag = False

    max_cnt = max(max_cnt, cnt)

print(max_cnt)