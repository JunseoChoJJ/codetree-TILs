n = int(input())

offset = 100

rectangle = [[0] * 201 for _ in range(201)]

for _ in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    x1, y1 = x1 + offset, y1 + offset
    x2, y2 = x2 + offset, y2 + offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            rectangle[x][y] = 1

area = 0
for x in range(201):
    for y in range(201):
        if rectangle[x][y] == 1:
            area += 1

print(area)