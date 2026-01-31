n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dx = [0,1,0,-1]
dy = [1,0,-1,0]

direction = 0
num = 1
startX = 0
startY = 0

for _ in range(n*m):

    arr[startX][startY] = num
    nx = startX + dx[direction]
    ny = startY + dy[direction]

    if (nx < 0 or ny < 0 or nx >= n or ny >= m) or arr[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx = startX + dx[direction]
        ny = startY + dy[direction]
    
    startX = nx
    startY = ny
    num += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()