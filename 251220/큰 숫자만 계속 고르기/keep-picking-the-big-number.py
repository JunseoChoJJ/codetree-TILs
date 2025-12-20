import heapq
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
pq = []

for num in arr:
    heapq.heappush(pq, -num)

for _ in range(m):
    maxNum = pq[0]
    heapq.heappop(pq)
    heapq.heappush(pq, maxNum+1)
    
    
print(-pq[0])