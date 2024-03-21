n,m,k = map(int, input().split())
n_list = [0] * (n+1)
ans = 0
for i in range(m):
    num = int(input())

    n_list[num] += 1

    if n_list[num] == k:
        ans = num
        break

if ans == 0:
    print(-1)
else:
    print(ans)