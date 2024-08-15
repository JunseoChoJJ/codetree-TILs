m = int(input())
a, b = map(int, input().split())

ans=[]
for num in range(a, b+1):
    
    left = 1
    right = m
    cnt = 1

    while left <= right:
        mid = (left + right) // 2

        if mid == num:
            ans.append(cnt)
            break
        
        if mid > num:
            right = mid - 1
        else:
            left = mid+1

        cnt += 1

print(min(ans), max(ans))