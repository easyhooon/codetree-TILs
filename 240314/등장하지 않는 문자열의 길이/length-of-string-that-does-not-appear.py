import sys

si = sys.stdin.readline

n = int(si())
arr = list(si().strip())

answer = 1

for i in range(1, n):
    twice = False

    for j in range(n - i + 1):
        for k in range(j + 1, n - i + 1):
            # is_same : j부터 i길이의 부분 문자열과
            # k부터 i길이의 부분 문자열이 완전히 같으면 true
            is_same = True

            for l in range(i):
                if arr[j + l] != arr[k + l]:
                    is_same = False

            if is_same:
                twice = True
    if twice:
        answer = i + 1
    else:
        break

print(answer)