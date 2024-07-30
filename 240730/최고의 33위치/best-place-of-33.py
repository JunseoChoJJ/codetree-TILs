n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# 
cnt = 0
if n == 2 or n == 3:
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1
else:
    for i in range(n-2):
        for j in range(n-2):
            tmp = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i+2][j] + board[i+2][j+1] + + board[i+2][j+2]
            cnt = max(cnt, tmp)
        


print(cnt)