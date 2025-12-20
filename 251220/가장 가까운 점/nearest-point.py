import heapq
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
pq = []

for x, y in points:
    heapq.heappush(pq, (x+y, x, y))


for _ in range(m):
    minSum, minX, minY = pq[0]
    x = minX + 2
    y = minY + 2

    heapq.heappop(pq)
    heapq.heappush(pq, (x+y, x, y))

_, ansX, ansY = pq[0]
print(ansX, ansY)