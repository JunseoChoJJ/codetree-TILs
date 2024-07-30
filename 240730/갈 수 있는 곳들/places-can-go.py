from collections import deque
n, k = map(int, input().split())
board=[]
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for _ in range(k):
    r, c = map(int, input().split())

    q = deque([(r-1, c-1)])
    visited[r-1][c-1] = 1
    while q:
        (nowY, nowX) = q.popleft()

        for i in range(4):
            ny = nowY + dy[i]
            nx = nowX + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if visited[ny][nx] == 1: continue
            if board[ny][nx] == 1: continue
            visited[ny][nx] = 1
            q.append((ny, nx))

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)