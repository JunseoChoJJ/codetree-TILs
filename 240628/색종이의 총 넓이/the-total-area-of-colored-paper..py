offset = 100

rec = [[0] * 201 for _ in range(201)]

n = int(input())

for _ in range(n):
    x1, y1 = map(int, input().split())
    x1, y1 = x1 + offset, y1 + offset

    for x in range(x1, x1+8):
        for y in range(y1, y1+8):
            rec[x][y] = 1

area = 0

for x in range(201):
    for y in range(201):
        if rec[x][y] == 1:
            area += 1

print(area)