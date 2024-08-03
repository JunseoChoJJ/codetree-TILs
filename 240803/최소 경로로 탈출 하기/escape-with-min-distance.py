from collections import deque
n, m = map(int, input().split())
board=[]
for _ in range(n):
    board.append(list(map(int, input().split())))


dy = [-1,1,0,0]
dx = [0,0,-1,1]

q = deque([(0, 0)])
visited = [[0] * m for _ in range(n)]
    
while q:
    (nowY, nowX) = q.popleft()

    if nowY == (n-1) and nowX == (m-1):
        print(board[nowY][nowX] - 1)
        break
    for i in range(4):
        ny = nowY + dy[i]
        nx = nowX + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
        if board[ny][nx] == 0: continue
        if visited[ny][nx] == 1: continue
        visited[ny][nx] = 1
        board[ny][nx] = board[nowY][nowX] + 1
        q.append((ny, nx))