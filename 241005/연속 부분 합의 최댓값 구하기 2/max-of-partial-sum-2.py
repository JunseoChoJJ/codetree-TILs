n = int(input())
nList = list(map(int, input().split()))



total = 0

for num in nList:
    if total < 0:
        total = 0
    total += num
    

print(total)