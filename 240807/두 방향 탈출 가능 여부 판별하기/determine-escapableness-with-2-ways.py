n, m = map(int, input().split())
board=[]

for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
dy = [0,1]
dx = [1,0]

def dfs(y, x):
    

    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
        if visited[ny][nx] == 1: continue
        if board[ny][nx] == 0: continue
        visited[ny][nx] = 1
        dfs(ny, nx)





visited[0][0] = 1
dfs(0,0)

print(visited[n-1][m-1])