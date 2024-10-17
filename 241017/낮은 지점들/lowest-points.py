n = int(input())

d = dict()


for _ in range(n):
    x, y = map(int, input().split())

    if x not in d:
        d[x] = y
    else:
        if d[x] >= y:
            d[x] = y

total = 0
for x, y in d.items():
    total += y

print(total)