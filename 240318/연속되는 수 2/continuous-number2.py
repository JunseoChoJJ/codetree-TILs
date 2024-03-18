n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
cnt = 0
tmp = 0

for j in range(n):
    if j == 0 or a[j] != a[j-1]:
        if cnt > tmp:
            tmp = cnt
        cnt = 1
    else:
        cnt += 1
print(tmp)