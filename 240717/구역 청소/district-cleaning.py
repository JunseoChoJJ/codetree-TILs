a, b = map(int, input().split())
c, d = map(int, input().split())

check = [0] * 101

for i in range(a, b):
    check[i] = 1
for j in range(c, d):
    check[j] = 1
ans = 0
for k in range(0, 101):
    if check[k] == 1:
        ans += 1

print(ans)