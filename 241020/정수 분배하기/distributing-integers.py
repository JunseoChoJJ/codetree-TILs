import sys
n, m = map(int, input().split())
nList = []
for _ in range(n):
    num = int(input())
    nList.append(num)



maxSize = sum(nList) // 11

def isPossible(maxSize):

    cnt = 0

    for elem in nList:    
        cnt += elem // maxSize
    
    return cnt


left = 1
right = maxSize

ans = 0

while left <= right:
    mid = (left + right) // 2
    if isPossible(mid) == m:
        ans = max(ans, mid)
        left = mid + 1
    
    if isPossible(mid) < m:
        right = mid - 1
    else:
        left = mid + 1
    

print(ans)