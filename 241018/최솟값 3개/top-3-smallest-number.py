n = int(input())
nList = list(map(int, input().split()))

if n < 4:
    print(-1)
else:
    nList.sort()
    print(nList[0] * nList[1] * nList[2])