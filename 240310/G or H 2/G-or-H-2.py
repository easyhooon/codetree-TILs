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
start = 0
end = max_coord
while start <= end: