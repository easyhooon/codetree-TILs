import sys

si = sys.stdin.readline

n, m = tuple(map(int, si().split()))
combination = []
    
def find_combination(curr_num, cnt):
    if cnt > m:
        return 

    if curr_num == n + 1:
        if cnt == m:
            for elem in combination:
                print(elem, end = " ")
            print()
        return

    combination.append(curr_num)
    find_combination(curr_num + 1, cnt + 1)
    combination.pop()

    find_combination(curr_num + 1, cnt)


find_combination(1, 0)