from sortedcontainers import SortedSet

n, k = map(int, input().split())
nList = list(map(int, input().split()))

s = SortedSet(nList)


length = len(s)

for _ in range(k):
    print(s[-1], end = " ")
    s.remove(s[-1])