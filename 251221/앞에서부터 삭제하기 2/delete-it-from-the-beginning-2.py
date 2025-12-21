import heapq
n = int(input())
arr = list(map(int, input().split()))

pq = []
# Please write your code here.
k = n-1

for num in range(1,k):
    minNum = min(arr[num:])
    total2 = sum(arr[num:])
    total = total2 - minNum
    length = n - num - 1
    
    avg = round(total / length, 2)
    
    heapq.heappush(pq, -avg)

maxAvg = -pq[0]
print(f"{maxAvg:.2f}")