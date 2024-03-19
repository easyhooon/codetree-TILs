import sys

si = sys.stdin.readline

n, m = map(int, si().split())

a = [
    si().strip()
    for _ in range(n)
]

b = [
    si().strip()
    for _ in range(n)
]

answer = 0
s = set()

def test_location(x, y, z):
    s.clear()
    
    for i in range(n):
        s.add(a[i][x] + a[i][y] + a[i][z])

    for i in range(n):
        if (b[i][x] + b[i][y] + b[i][z]) in s:
            return False 

    return True 

for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            if test_location(i, j, k):
                answer += 1

print(answer)