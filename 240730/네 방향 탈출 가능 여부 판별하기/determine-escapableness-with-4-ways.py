from collections import deque
n, m = map(int, input().split())
board=[]
visited=[[0] * m for _ in range(n)] 
for _ in range(n):
    board.append(list(map(int, input().split())))

startY, startX = 0, 0
endY, endX = n-1, m-1

dy = [-1,1,0,0]
dx = [0,0,-1,1]

q = deque([(startY, startX)])
check = False
while q:
    (nowY, nowX) = q.popleft()
    visited[startY][startX] = 1

    for i in range(4):
        ny = nowY + dy[i]
        nx = nowX + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
        if visited[ny][nx] == 1: continue
        visited[ny][nx] = 1
        if board[ny][nx] == 0: continue
        q.append((ny, nx))
        if ny == endY and nx == endX: 
            check = True
if check == True:
    print(1)
else:
    print(0)