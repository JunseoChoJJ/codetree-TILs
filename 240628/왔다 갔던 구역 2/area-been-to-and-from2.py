n = int(input())

n_list = [0] * 2001

mid = 1000

for _ in range(n):
    a, b = map(str, input().split())
    a = int(a)

    if b == "R":
        a += mid
        for i in range(mid, a):
            n_list[i] += 1
        mid = a
    else:
        a = mid - a
        for i in range(a, mid):
            n_list[i] += 1
        mid = a

cnt = 0
for num in n_list:
    if num >= 2: 
        cnt += 1

print(cnt)