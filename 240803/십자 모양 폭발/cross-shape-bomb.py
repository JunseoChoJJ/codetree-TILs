n = int(input())
board=[]
for _ in range(n):
    board.append(list(map(int, input().split())))

r, c = map(int, input().split())

bomb = board[r-1][c-1]


dy = [-1,1,0,0]
dx = [0,0,-1,1]


# bomb
board[r-1][c-1] = 0
if bomb != 1: 
    for i in range(1, bomb):
        for j in range(4):
            ny = i * dy[j] + (r-1)
            nx = i * dx[j] + (c-1)

            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            board[ny][nx] = 0
# gravity
tmp = [[0] * n for _ in range(n)] 


for column in range(n):
    tmp_row = n-1
    for row in range(n-1,-1,-1):
        if board[row][column] != 0:
            tmp[tmp_row][column] = board[row][column]
            tmp_row -= 1

board = tmp

for row in range(n):
    for column in range(n):
        print(board[row][column], end=' ')
    print()