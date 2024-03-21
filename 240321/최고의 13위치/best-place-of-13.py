n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
max_cnt = 0
for i in range(n):
    for j in range(n-2):
        max_cnt = max(max_cnt, board[i][j] + board[i][j+1] + board[i][j+2])
print(max_cnt)