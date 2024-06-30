n = int(input())

point = []
for _ in range(n):
    x, y = map(int, input().split())
    point.append((x, y))


ans = float("inf")
for i in range(n):
    min_y = 40001
    max_y = 0
    min_x = 40001
    max_x = 0
    for j in range(n):    
        if i == j: continue
        max_x = max(max_x, point[j][0])
        max_y = max(max_y, point[j][1])
        min_y = min(min_y, point[j][1])
        min_x = min(min_x, point[j][0])
    
    rec = (max_x - min_x) * (max_y - min_y)
    ans = min(ans, rec)

print(ans)