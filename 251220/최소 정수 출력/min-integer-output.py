import heapq
n = int(input())
x = [int(input()) for _ in range(n)]
pq = []
# Please write your code here.
for num in x:
    
    if num == 0:
        if pq:
            print(pq[0])
            heapq.heappop(pq)
        else:
            print(0)
    else:
        heapq.heappush(pq, num)