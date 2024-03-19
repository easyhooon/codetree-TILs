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
        s.add(a[i][x:x + 1] + a[i][y:y + 1] + a[i][z:z + 1])

    for i in range(n):
        if (b[i][x:x + 1] + b[i][y:y + 1] + b[i][z:z + 1]) in s:
            return False 

    return True 

for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            if test_location(i, j, k):
                answer += 1

print(answer)