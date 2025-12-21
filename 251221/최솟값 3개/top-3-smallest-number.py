import heapq
n = int(input())
arr = list(map(int, input().split()))
pq = []
# Please write your code here.


for num in arr:
    heapq.heappush(pq, num)

    if len(pq) < 3:
        print(-1)
        continue

    firstNum = pq[0]
    heapq.heappop(pq)
    secondNum = pq[0]
    heapq.heappop(pq)
    thirdNum = pq[0]

    print(firstNum * secondNum * thirdNum)
    heapq.heappush(pq, firstNum)
    heapq.heappush(pq, secondNum)