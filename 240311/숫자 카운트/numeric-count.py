import sys

si = sys.stdin.readline

n = int(si())

# flag = [True] * 1000

# for _ in range(n):
#     num, cnt_1, cnt_2 = map(int, si().split())
#     if cnt_1 == 3:
#         print(1)
#         sys.exit(0)
#     else if cnt_1 == 2 and cnt_2 = 1:
    
#     else if cnt_1 == 2 and cnt_2 = 0:

#     else if cnt_1 == 1 and cnt_2 = 2:

#     else if cnt_1 == 1 and cnt_2 = 1:

#     else if cnt_1 == 1 and cnt_2 = 0:

#     else:
#         # 모든 숫자가 같지 않고, 다른 위치에 있는 것도 없음 
#         for i in range(100, 1000):
#             if str(num[0]) in str(i) or str(num[1]) in str(i) or str(num[2]) in str(i):
#                 flag[i] = False

# cnt = 0
# for i in range(100, 1000):
#     if flag[i] and str(i)[0] != str(i)[1] and str(i)[0] != str(i)[2] and str(i)[1] != str(i)[2]:
#         cnt += 1

# print(cnt)

arr = [
    list(map(int, si().split()))
    for _ in range(n)
]

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue

            flag = True
            for a, num_cnt1, num_cnt2 in arr:
                x = a // 100
                y = a // 10 % 10
                z = a % 10

                cnt1 = 0
                cnt2 = 0

                if x == i:
                    cnt1 += 1

                if y == j:
                    cnt1 += 1

                if z == k:
                    cnt1 += 1

                if x == j or x == k:
                    cnt2 += 1

                if y == i or y == k:
                    cnt2 += 1

                if z == i or z == j:
                    cnt2 += 1
                
                # 카운트 수가 다르면 해당 숫자는 정답이 될 수 없음 
                if cnt1 != num_cnt1 or cnt2 != num_cnt2:
                    flag = False
                    break

            if flag:
                # print(i * 100 + j * 10 + k)
                cnt += 1

print(cnt)