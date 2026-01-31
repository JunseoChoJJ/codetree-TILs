n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

# Please write your code here.
dx = [1,0,-1,0]
dy = [0,1,0,-1]


num = 1
startX = 0
startY = 0
dir = 0
for i in range(n*m):
    grid[startX][startY] = num

    nx = startX + dx[dir]
    ny = startY + dy[dir]

    if (nx < 0 or ny < 0 or nx >= n or ny >= m) or grid[nx][ny] != 0:
        dir = (dir + 1) % 4
        nx = startX + dx[dir]
        ny = startY + dy[dir]

    startX = nx
    startY = ny
    num += 1

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()