from sortedcontainers import SortedSet


n, m = map(int,input().split())
mList = list(map(int, input().split()))
s = SortedSet()

for i in range(1, m+1):
    s.add(i)


for num in mList:

    s.remove(num)
    print(s[-1])