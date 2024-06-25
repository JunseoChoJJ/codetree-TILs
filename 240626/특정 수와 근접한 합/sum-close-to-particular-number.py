n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 100


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                total = arr[i] + arr[j] + arr[k] + arr[l]

                ans = min(ans, abs(total - s))

print(ans)