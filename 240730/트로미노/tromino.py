n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))



max_ans = 0

for row in range(n):
    for column in range(m):
        if row + 1 >=n or column + 1 >= m: continue
        block1 = board[row][column] + board[row+1][column] + board[row+1][column+1]
        block2 = board[row][column] + board[row][column+1] + board[row+1][column]
        block3 = board[row][column] + board[row][column+1] + board[row+1][column+1]
        block4 = board[row][column+1] + board[row+1][column+1] + board[row+1][column]
        max_ans = max(max_ans, block1,block2,block3,block4)
        if row + 2 >= n and column + 2 >= m: continue
        block5, block6 = 0,0
        if row + 2 >= n and column + 2 < m:
            block5 = board[row][column] + board[row][column+1] + board[row][column+2]
        if row + 2 <= n and column + 2 > m:
            block6 = board[row][column] + board[row+1][column] + board[row+2][column]                                          
        max_ans = max(max_ans, block5, block6)

print(max_ans)