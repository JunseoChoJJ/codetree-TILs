from sortedcontainers import SortedSet


n,m = map(int, input().split())
nList = list(map(int, input().split()))

s = SortedSet(nList)


for _ in range(m):
    num = int(input())

    if s.bisect_left(num) < len(s):
        idx = s.bisect_left(num)
        print(s[idx])
    else:
        print(-1)