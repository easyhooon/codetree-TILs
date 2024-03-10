import sys

si = sys.stdin.readline

n = int(si())

# G -> 1, H -> 2
temp = []
max_coord = -sys.maxsize
for _ in range(n):
    coord, alphabet = map(str, si().split())
    max_coord = max(max_coord, int(coord))
    if alphabet == 'G':
        temp.append((int(coord), 1))
    else:
        temp.append((int(coord), 2))

arr = [0] * (max_coord + 1)

for coord, alphabet in temp:
    arr[coord] = alphabet

# 투포인터 풀듯이 풀어보자
# 근데 어디서 만나는지 그런게 중요한게 아닌데,,
max_len = 0
for i in range(max_coord + 1):
    for j in range(i + 1, max_coord + 1):
        if arr[i] == 0 or arr[j] == 0:
            continue

        cnt_g = 0
        cnt_h = 0

        for k in range(i, j + 1):
            if arr[k] == 1:
                cnt_g += 1
            if arr[k] == 2:
                cnt_h += 1

        if cnt_g == cnt_h:
            len_val = j - i
            max_len = max(max_len, len_val)

print(max_len)