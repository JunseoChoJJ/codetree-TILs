n, k = map(int,input().split())
arr = list(map(int, input().split()))

count = dict()

for elem in arr:
    if elem not in count:
        count[elem] = 1
    else:
        count[elem] += 1

ans = 0

for num in count:
    ans = max(ans, count[num])
possible = []
for num in count:
    if count[num] == ans:
        possible.append(num)


possible.sort()

for i in range(len(possible)-1,-1,-1):
    print(possible[i], end = ' ')