n = int(input())
y, x  = map(int, input().split())
board=[]
for _ in range(n):
    board.append(list(input()))
x = x-1
y = y-1


# ans variable
time = 0 
check = False
dy = [0,1,0,-1]
dx = [1,0,-1,0]
direction = 0
cnt = 0

while True:
    if time > n * n or cnt == 4:
        break

    ny = y + dy[direction]
    nx = x + dx[direction]
    # 1st case
    if ny < 0 or nx < 0 or ny >= n or nx >= n:
        time += 1
        check = True
        break
    elif board[ny][nx] == '#':
        direction = (direction + 3)  % 4
        cnt += 1
    
    # 2nd case
    

    # 3rd case and 4th case
    else: 
        direction += 1
        direction = direction % 4
        check_y = ny + dy[direction]
        check_x = nx + dx[direction]
        if board[check_y][check_x] == '.':
            y = check_y
            x = check_x
            time += 2
        else:
            y = ny
            x = nx
            if direction == 0:
                    direction = 3
            else:
                direction -= 1
            time += 1
        cnt = 0

if check == False:
    print(-1)
else:
    print(time)