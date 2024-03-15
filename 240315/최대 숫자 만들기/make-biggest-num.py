import sys
from functools import cmp_to_key

si = sys.stdin.readline

# custom comparator를 직접 정의
# x가 앞에 있는 숫자, y가 뒤에 있는 숫자 가정했을 때
# 이 순서가 우리가 원하는 순서라면 0보다 작은 값을,
# 반대라면 0보다 큰 값을
# 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
# 보통 반환값에 1, -1, 0을 사용합니다.
def compare(x, y):
    # x가 y보다 크다면
    # 우리가 원하는 방향입니다.
    if int(str(x) + str(y)) > int(str(y) + str(x)):
        return -1
    # y가 x보다 크다면
    # 우리가 원하지 않는 방향입니다.
    if int(str(y) + str(x)) > int(str(x) + str(y)):
        return 1
    # 우선 순위가 동일한 경우입니다.
    return 0


n = int(si())
a = list(int(si()) for _ in range(n))

# 내림차순 정렬
a.sort(key=cmp_to_key(compare))

# print(a)

for elem in a:  # 정렬 이후의 결과 출력
    print(elem, end="")