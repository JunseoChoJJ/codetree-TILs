from sortedcontainers import SortedSet
import sys
s = SortedSet()


n = int(input())
nList = list(map(int, input().split()))

s.add(0)

ans = sys.maxsize
for num in nList:
    s.add(num)

    idx = s.bisect_right(num)
    

    if idx == len(s):
        diff = s[idx-1] - s[idx-2]
        ans = min(ans, diff)
    else:
        diff1 = s[idx] - s[idx-1]
        diff2 = s[idx-1] - s[idx-2]
        ans = min(ans, diff1, diff2)

    print(ans)