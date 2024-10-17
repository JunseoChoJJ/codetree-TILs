# 다시 풀어보기

import heapq
n = int(input())
nList = list(map(int, input().split()))

pq = []

for num in nList:
    heapq.heappush(pq, -num)


while True:
    if len(pq) < 2:
        break

    first = pq[0]
    heapq.heappop(pq)
    second = pq[0]
    heapq.heappop(pq)

    diff = first - second
    if diff != 0:
        heapq.heappush(pq, diff)
        
if not pq:
    print(-1)
else:
    print(-pq[0])