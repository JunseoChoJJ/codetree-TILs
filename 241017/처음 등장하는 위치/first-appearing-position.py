from sortedcontainers import SortedDict

n = int(input())
nList = list(map(int, input().split()))

sd = SortedDict()

for i in range(1, n+1):

    if nList[i-1] not in sd:
        sd[nList[i-1]] = i


for key, value in sd.items():
    print(key, value)