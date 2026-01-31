n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]


# Please write your code here.
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

startX = 0
startY = 0
di = 0
alphabetNum = 0
for i in range(n*m):
    grid[startX][startY] = alphabet[alphabetNum]
    nx = startX + dxs[di]
    ny = startY + dys[di]

    if (nx < 0 or ny < 0 or nx >= n or ny >= m) or grid[nx][ny] != 0:
        di = (di + 1) % 4
        nx = startX + dxs[di]
        ny = startY + dys[di]

    startX = nx
    startY = ny
    alphabetNum = (alphabetNum + 1) % 26


for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()