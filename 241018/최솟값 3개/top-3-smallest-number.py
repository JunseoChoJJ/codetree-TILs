import heapq
n = int(input())
nList = list(map(int, input().split()))


pq = []

for i in range(n):
    if i < 2:
        print(-1)
        heapq.heappush(pq, nList[i])
    else:
        heapq.heappush(pq, nList[i])
        first = heapq.heappop(pq)
        second = heapq.heappop(pq)
        third = heapq.heappop(pq)
        print(first * second * third)
        heapq.heappush(pq, first)
        heapq.heappush(pq, second)
        heapq.heappush(pq, third)