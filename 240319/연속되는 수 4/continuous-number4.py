n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

ans = 0
cnt = 0

for i in range(n):
    if i == 0 or a[i] <= a[i-1]:
        cnt = 1
    else:
        cnt += 1
    ans = max(ans, cnt)

print(ans)