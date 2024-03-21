n = int(input())
n_list = list(map(int, input().split()))

ans = 0
for i in range(len(n_list)):
    total = 0
    for j in range(i+2, len(n_list)):
        total = n_list[i] + n_list[j]
        ans = max(ans, total)
print(ans)