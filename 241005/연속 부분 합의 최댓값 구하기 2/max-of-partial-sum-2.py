n = int(input())
nList = list(map(int, input().split()))



total = 0

for num in nList:
    total += num
    if total < 0:
        total = 0

print(total)