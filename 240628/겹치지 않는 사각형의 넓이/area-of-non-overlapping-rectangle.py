offset = 1000
rec = [[0] * 2001 for _ in range(2001)]


for i in range(3):
    x1,y1,x2,y2 = map(int, input().split())
    x1, x2 = x1 + offset, x2+offset
    y1, y2 = y1 + offset, y2+offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            if i == 2:
                rec[x][y] = 0
            else:
                rec[x][y] = 1
area = 0
for x in range(2001):
    for y in range(2001):
        if rec[x][y] == 1:
            area += 1


print(area)