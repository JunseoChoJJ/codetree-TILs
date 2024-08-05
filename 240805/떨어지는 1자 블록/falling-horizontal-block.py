n, m, k = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

tmp_row = 1
check = False

while True:
    if check == True:
        break

    for col in range(k-1, k+m-1):
        if board[tmp_row][col] == 1:
            check = True
            break

    if check == True:
        for column in range(k-1, k+m-1):
            board[tmp_row-1][column] = 1
    else:
        tmp_row += 1
    



for row in range(n):
    for column in range(n):
        print(board[row][column], end = ' ')
    print()