import string
n, m = map(int, input().split())

board = [[0] * m for _ in range(n)]
check = [[0] * m for _ in range(n)]
alphabet = list(string.ascii_uppercase)


dy = [0,1,0,-1]
dx = [1,0,-1,0]
start = 0
y, x = 0,0
dirs = 0

for _ in range(n*m):

    board[y][x] = alphabet[start]
    start += 1
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

    if start == 26:
        start = 0

for i in range(n):
    for j in range(m):
        print(board[i][j], end = " ")
    print()