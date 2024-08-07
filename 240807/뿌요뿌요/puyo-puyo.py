n = int(input())
board=[]

for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]
dy = [0,0,-1,1]
dx = [1,-1,0,0]

cnt = 0
def dfs(y, x):
    visited[y][x] = 1
    size= board[y][x]
    global cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        if visited[ny][nx] == 1: continue
        if board[ny][nx] != size: continue
        visited[ny][nx] = 1
        cnt += 1
        dfs(ny, nx)

block=[0] * 101



for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt = 1
            dfs(i, j)
            if cnt >= 4:
                
                block[board[i][j]] = cnt

max_index=0
max_num = 0
for i in range(101):
    if block[i] > max_num:
        max_num = block[i]
        max_index = i

print(max_index, max_num)