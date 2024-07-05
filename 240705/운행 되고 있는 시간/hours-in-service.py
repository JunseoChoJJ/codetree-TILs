n = int(input())

n_list = []
for _ in range(n):
    a, b = map(int, input().split())
    n_list.append((a,b))

ans = -1

for i in range(n):
    work= [0] * 1000
    for j in range(n):
        if i == j: continue
        x = n_list[j][0]
        y = n_list[j][1]
        for k in range(x, y):
            work[k] = 1
    
    cnt = work.count(1)
    ans = max(ans, cnt)
print(ans)