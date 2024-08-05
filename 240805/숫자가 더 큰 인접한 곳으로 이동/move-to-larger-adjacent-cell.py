n, r, c = map(int, input().split())

board=[]

for _ in range(n):
    board.append(list(map(int, input().split())))

dy = [-1,1,0,0]
dx = [0,0,-1,1]

curr_y = r-1
curr_x = c-1

while True:
    max_num = board[curr_y][curr_x]
    print(max_num, end = ' ')
    
    cnt = 0
    for i in range(4):
        ny = curr_y + dy[i]
        nx = curr_x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        if board[ny][nx] > max_num:
            max_num = board[ny][nx]
            curr_y = ny
            curr_x = nx
            cnt += 1
            break
    if cnt == 0:
        break