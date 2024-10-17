n, m = map(int, input().split())
nList = list(map(int, input().split()))
mList = list(map(int, input().split()))
di = dict()



for num in nList:
    if num not in di:
        di[num] = 1
    else:
        di[num] += 1


for q in mList:
    if q in di:
        print(di[q], end = ' ')
    else:
        print(0, end = ' ')