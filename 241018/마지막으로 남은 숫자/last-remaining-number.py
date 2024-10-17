import heapq
n = int(input())
nList = list(map(int, input().split()))

pq = []

for num in nList:
    heapq.heappush(pq, -num)


while True:
    if len(pq) == 1:
        print(-pq[0])
        break

    first = pq[0]
    heapq.heappop(pq)
    second = pq[0]
    heapq.heappop(pq)

    diff = first - second
    if diff != 0:
        heapq.heappush(pq, diff)