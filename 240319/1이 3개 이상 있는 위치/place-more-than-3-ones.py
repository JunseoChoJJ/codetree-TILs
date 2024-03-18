n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dy = [0,0,-1,1]
dx = [-1,1,0,0]
ans = 0
ny, nx = 0, 0
while True:
    cnt = 0
    for k in range(4):
        ny1 = ny + dy[k]
        nx1 = nx + dx[k]

        if ny1 < 0 or nx1 < 0 or ny1 >= n or nx1 >= n: continue
        if board[ny1][nx1] == 1:
            cnt += 1
    if cnt >= 3:
        ans += 1        
    if ny == (n - 1) and nx == (n - 1):
        break
    if nx == (n - 1):
        nx = 0
        ny += 1
    else:
        nx += 1
print(ans)