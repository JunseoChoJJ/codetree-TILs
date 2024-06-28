offset = 1000
rec = [[0] * 2001 for _ in range(2001)]


for i in range(2):
    x1,y1,x2,y2 = map(int, input().split())

    x1,x2 = x1+offset,x2+offset
    y1,y2 = y1+offset,y2+offset

    for x in range(x1, x2):
        for y in range(y1, y2):
            if i == 0:
                rec[x][y] = 1
            else:
                rec[x][y] = 0

max_x = 0
min_x = 2002
max_y = 0
min_y = 2002
for x in range(2001):
    for y in range(2001):
        if rec[x][y] == 1:
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)


if min_x == 2002:
    min_x = 1
if min_y == 2002:
    min_y = 1
x = max_x - min_x + 1
y = max_y - min_y + 1
print(x*y)