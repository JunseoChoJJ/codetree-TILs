n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
d = {}


for x,y in points:
    if x in d:
        if d[x] > y:
            d[x] = y
    else:
        d[x] = y
total = 0
for num in d:
    total += d[num]
print(total)