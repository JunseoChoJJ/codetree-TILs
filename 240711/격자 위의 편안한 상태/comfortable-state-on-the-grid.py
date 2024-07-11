n, m = map(int, input().split())
board = [[0] * n for _ in range(n)]

dy = [0,0,-1,1]
dx = [-1,1,0,0]

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    
    cnt = 0
    board[r][c] = 1
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]

        if nr < 0 or nc < 0 or nr >= n or nc >= n: continue
        if board[nr][nc] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)