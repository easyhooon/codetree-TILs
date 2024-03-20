import sys

si = sys.stdin.readline

n = int(si())
arr = []
answer = 0

for _ in range(n):
    x1, x2 = map(int, si().split())
    arr.append((x1, x2))

choose_num = []

def check():
    flag = True
    if choose_num:
        end_point = arr[choose_num[0]][1]
        for i in range(1, len(choose_num)):
            if end_point >= arr[choose_num[i]][0]:
                return False
            else:
                end_point = arr[choose_num[i]][1]

        if flag:
            return True

    else:
        return True


def choose(curr_num):
    global answer
    if curr_num == n:
        if check():
            answer = max(answer, len(choose_num))
        return
    
    choose_num.append(curr_num)
    choose(curr_num + 1)
    choose_num.pop()

    choose(curr_num + 1)


choose(0)
print(answer)