n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
cnt = 0

for i in range(1, n+1):
    if arr[i-1] == 0:
        arr[i-1] = 1
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = 0
        if arr[i+1] == 0:
            arr[i+1] = 1
        else:
            arr[i+1] = 0

        cnt += 1
if arr.count(1) == n:
    print(cnt)
else:
    print(-1)