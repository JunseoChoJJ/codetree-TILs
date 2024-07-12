n, t = map(int, input().split())
orders = list(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[0] * n for _ in range(n)]
mid = n // 2
y, x = mid, mid
ans = board[y][x]

dirs = 0 
dy = [-1,0,1,0]
dx = [0,1,0,-1]


for i in range(t):
    order = orders[i]

    if order == 'R':
        dirs = (dirs + 1) % 4
    elif order == 'L':
        dirs = (dirs + 3) % 4
    else:
        ny = y + dy[dirs]
        nx = x + dx[dirs]

        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        ans += board[ny][nx]
        y = ny
        x = nx
print(ans)