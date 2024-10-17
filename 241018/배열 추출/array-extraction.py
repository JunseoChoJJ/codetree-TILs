import heapq

n = int(input())

pq = []

for _ in range(n):
    num = int(input())
    num = -num
    if num == 0:
        if not pq:
            print(0)            
        else:
            print(-pq[0])
            heapq.heappop(pq)

    else:
        heapq.heappush(pq, num)