import sys

si = sys.stdin.readline

N = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(N)
]
new_arr = []


for i in range(1, N - 1):
    temp = arr[i]
    arr.remove(temp)
    ans = 0
    for j in range(N - 2):
        distance = abs(arr[j][0] - arr[j + 1][0]) + abs(arr[j][1] - arr[j + 1][1])
        ans += distance
    new_arr.append(ans)
    arr.insert(i, temp)

print(min(new_arr))