n, t = map(int, input().split())
n_list = list(map(int, input().split()))

cnt, ans = 0, 0
for i in range(n):
    if n_list[i] <= t:
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)