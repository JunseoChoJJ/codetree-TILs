n = int(input())
nList = list(map(int, input().split()))

k = n - 2
ans = 0

for i in range(1, k + 1):
    mList = nList[i:]
    
    lowNum = min(mList)
    total = sum(mList) - lowNum
    pos = total / (len(mList) - 1)
    ans = max(ans, pos)

print(f"{ans:.2f}")