from sortedcontainers import SortedDict
n = int(input())
arr = list(map(int, input().split()))
sd = SortedDict()

# Please write your code here.
for i, a in enumerate(arr):
    if a not in sd:
        sd[a] = i+1

for key, value in sd.items():
    print(key, value)