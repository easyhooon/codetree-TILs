import sys

si = sys.stdin.readline

n = int(si())

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

answer = 0
for i in range(11):
    for j in range(11):
        for k in range(11):
            success = True
            for x, y in arr:
                if x == i or x == j or x == k:
                    continue
                
                success = False
            if success:
                answer = 1

            success = True 
            for x, y in arr:
                if x == i or x == j or y == k:
                    continue
                
                success = False
            if success:
                answer = 1

            success = True
            for x, y in arr:
                if x == i or y == j or y == k:
                    continue

                success = False
            if success:
                answer = 1

            success = True
            for x, y in arr:
                if y == i or y == j or y == k:
                    continue
                
                success = False
            if success:
                answer = 1

print(answer)