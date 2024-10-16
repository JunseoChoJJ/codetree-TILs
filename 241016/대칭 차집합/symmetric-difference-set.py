a, b = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))


bigList = []

for i in range(len(aList)):
    bigList.append(aList[i])
    
for i in range(len(bList)):
    bigList.append(bList[i])

length = len(bigList)
intersection = set(bigList)

print(length - len(intersection))