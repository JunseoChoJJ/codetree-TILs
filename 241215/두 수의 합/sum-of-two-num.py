# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

d = dict()

for i in range(n):
    if arr[i] not in d:
        d[arr[i]] = 1


cnt = 0
for num in arr:
    remain = k - num
    if remain in d:
        cnt += 1

print(cnt // 2)

