n, m = map(int, input().split())

start = 0
y, x = 0, 0
dirs = 0
board = [[0] * m for _ in range(n)]
check = [[0] * m for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


for _ in range(n*m):
    start += 1
    board[y][x] = start
    check[y][x] = 1

    ny = y + dy[dirs]
    nx = x + dx[dirs]

    if ny < 0 or nx < 0 or ny >= n or nx >= m or check[ny][nx] == 1:
        dirs += 1
        if dirs == 4:
            dirs = 0
        y += dy[dirs]
        x += dx[dirs]
    else:
        y = ny
        x = nx
    
for i in range(n):
    for j in range(m):
        print(board[i][j], end = " ")
    print()