n, m = map(int, input().split())

dy = [0,1,0,-1]
dx = [1,0,-1,0]

direction = 0

board = [[0] * m for _ in range(n)]
ans = [[0] * m for _ in range(n)]

y, x = 0, 0
board[y][x] = 1
ans[y][x] = 1
for i in range(2, n*m + 1):
    ny = y + dy[direction]
    nx = x + dx[direction]
    if ny < 0 or nx < 0 or ny > (n - 1) or nx > (m - 1) or ans[ny][nx] == 1:
        direction = (direction + 1) % 4
        ny = y + dy[direction]
        nx = x + dx[direction]
        board[ny][nx] = i
        ans[ny][nx] = 1
        y = ny
        x = nx   
    else:
        board[ny][nx] = i
        ans[ny][nx] = 1
        y = ny
        x = nx
for i in range(n):
    for j in range(m):
        print(board[i][j], end = " ")
    print()