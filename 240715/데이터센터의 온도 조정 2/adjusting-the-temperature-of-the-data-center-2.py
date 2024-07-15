n,c,g,h = map(int, input().split())
n_list=[]
for _ in range(n):
    ta, tb = map(int, input().split())
    n_list.append((ta, tb))
ans = 0
for i in range(1001):

    cnt = 0
    for j in range(n):
        ta = n_list[j][0]
        tb = n_list[j][1]
        if i < ta:
            cnt += c
        elif i < tb:
            cnt += g
        else:
            cnt += h
    ans = max(ans, cnt)
print(ans)