n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

nList = set(nList)

for num in mList:
    if num in nList:
        print(1)
    else:
        print(0)