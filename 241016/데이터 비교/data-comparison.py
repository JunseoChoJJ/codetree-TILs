n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

for num in mList:
    if num in nList:
        print(1, end = ' ')
    else:
        print(0, end = ' ')