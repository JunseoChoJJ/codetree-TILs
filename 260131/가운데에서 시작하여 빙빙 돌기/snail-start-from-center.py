n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.


medium = n // 2

startX, startY = medium, medium

dxs = [0,-1,0,1]
dys = [1,0,-1,0]
direction =0



for i in range(n*n):
    if i == 0:
        num = 1
        grid[startX][startY] = num
    elif i == 1:
        startX += dxs[direction]
        startY += dys[direction]
        num += 1
        grid[startX][startY] = num
    else:
        direction = (direction + 1) % 4
        nx = startX + dxs[direction]
        ny = startY + dys[direction]
        num += 1
        


        if grid[nx][ny] == 0:
                grid[nx][ny] = num
        else:
            direction = (direction -1 + 4) % 4
            nx = startX + dxs[direction]
            ny = startY + dys[direction]
            grid[nx][ny] = num
            
        startX = nx
        startY = ny
    
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()