import sys

si = sys.stdin.readline

n = int(si())

a_arr = list(map(int, si().split()))
b_arr = list(map(int, si().split()))


if a_arr == b_arr:
    print(1)
else:
    cnt = 0
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if ((abs(i - a_arr[0]) <= 2 or abs(i - a_arr[0]) <= n - 2) and (abs(j - a_arr[1]) <= 2 or abs(j - a_arr[1]) <= n - 2) and (abs(k - a_arr[2]) <= 2 or abs(k - a_arr[2]) <= n - 2)) or ((abs(i - b_arr[0]) <= 2 or abs(i - b_arr[0]) <= n - 2) and (abs(j - b_arr[1]) <= 2 or abs(j - b_arr[1]) <= n - 2) and (abs(k - b_arr[2]) <= 2 or abs(k - b_arr[2]) <= n - 2)):
                    # print(i, j, k)
                    cnt += 1

    print(250 - cnt)