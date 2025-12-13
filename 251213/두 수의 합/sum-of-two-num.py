n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

d = {}

for num in arr:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
i = 0
cnt = 0
while True:

    if i == n:
        break
    diff = k - arr[i]
    
    if diff in d:
        cnt += d[diff]
    i += 1

print(cnt//2)