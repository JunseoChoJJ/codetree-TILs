n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
grid = [[0] * (n+1) for _ in range(n+1)]
dxs = [0,-1,0,1]
dys = [1,0,-1,0]

for i in range(m):
    x = points[i][0]
    y = points[i][1]
    cnt = 0
    grid[x][y] = 1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if nx < 1 or ny < 1 or nx > n or ny > n: continue
        if grid[nx][ny] == 1:
            cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)
    
