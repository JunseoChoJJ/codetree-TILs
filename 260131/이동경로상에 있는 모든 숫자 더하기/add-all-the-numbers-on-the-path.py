N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.


medium = N // 2
startX = medium
startY = medium

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
direction = 3


total = board[startX][startY]

for command in str:

    if command == "R":
        direction = (direction + 1) % 4
    elif command == "L":
        direction = (direction -1 + 4) % 4
    else:
        
        nx = startX + dxs[direction]
        ny = startY + dys[direction]

        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        total += board[nx][ny]
        startX = nx
        startY = ny
        


print(total)