import heapq
n = int(input())

pq = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(pq[0])
            heapq.heappop(pq)
    else:
        heapq.heappush(pq, num)