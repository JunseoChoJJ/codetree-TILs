n, k = map(int, input().split())
n_list = list(map(int, input().split()))

ans = 0
for i in range(n-k+1):
    max_val = 0
    for j in range(i, i+k):
        max_val += n_list[j]
    ans = max(ans, max_val)

print(ans)