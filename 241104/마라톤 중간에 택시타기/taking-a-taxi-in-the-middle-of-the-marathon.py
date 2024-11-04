import sys
n = int(input())

minDist = sys.maxsize

coordinate = []
for _ in range(n):
    x, y = map(int, input().split())

    coordinate.append(x, y)

l = []

for i in range(n):
    if i+1 == n:
        break
    x2 = coordinate[i+1][0]
    y2 = coordinate[i+1][0]
    
    diff = abs(coordinate[i][0] - x2) + abs(coordinate[i][1] - y2)
    l.append(diff)

print(l)