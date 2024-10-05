n = int(input())
nList = list(map(int, input().split()))



total = 0
possibleAns = []
for num in nList:
    if num < 0:
        if total > 0:
            possibleAns.append(total)
    if total < 0:
        total = 0
    total += num


possibleAns.append(total)



print(max(possibleAns))