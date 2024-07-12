n, k = map(int, input().split())

placed = [0] * 10000
for _ in range(n):
    location, alphabet = map(str, input().split())
    location = int(location)
    if alphabet == 'G':
        placed[location] = 1
    else:
        placed[location] = 2



ans = 0
for i in range(10000 - k):
    cnt = 0
    for j in range(i, i+k+1):
        cnt += placed[j]
    ans = max(ans, cnt)

print(ans)