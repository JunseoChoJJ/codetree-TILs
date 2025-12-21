import heapq
n = int(input())
arr = list(map(int, input().split()))
pq = []

for num in arr:
    heapq.heappush(pq, -num)

# Please write your code here.
while True:
    if len(pq) == 1:
        print(-pq[0])
        break
    if len(pq) == 0:
        print(-1)
        break

    firstNum = -pq[0]
    heapq.heappop(pq)
    secondNum = -pq[0]
    heapq.heappop(pq)
    
    if firstNum == secondNum:
        continue
    newNum = firstNum - secondNum
    
    heapq.heappush(pq, -newNum)

