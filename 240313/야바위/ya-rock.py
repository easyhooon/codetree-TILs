import sys

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

max_cnt = -sys.maxsize
for i in range(3):
    cnt = 0
    stone = [0] * 3
    stone[i] = 1
    for j in range(n):
        a, b, c = arr[j]
        a -= 1
        b -= 1
        c -= 1
        if stone[a] == 1:
            stone[a] = 0
            stone[b] = 1

        elif stone[b] == 1:
            stone[b] = 0
            stone[a] = 1

        if stone[c] == 1:
            cnt += 1

    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)