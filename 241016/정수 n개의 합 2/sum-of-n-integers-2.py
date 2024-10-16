n, k = map(int, input().split())
nList = list(map(int, input().split()))


prefix_sum = [0] * n



for i in range(n):
    if i+1 == n:
        break
    prefix_sum[i] = nList[i+1] + nList[i]


print(max(prefix_sum))