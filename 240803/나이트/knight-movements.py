from collections import deque
n = int(input())
r1,c1,r2,c2 = map(int, input().split())

visited = [[0] * n for _ in range(n)]
board = [[0] * n for _ in range(n)]

dy = [-1,-2,-2,-1,1,2,2,1]
dx = [-2,-1,1,2,-2,-1,1,2]

q = deque([(r1-1, c1-1)])
check = False
while q:
    (nowY, nowX) = q.popleft()
    
    if nowY == (r2-1) and nowX == (c2-1):
        check = True
        print(board[nowY][nowX])
        break

    for i in range(8):
        ny = nowY + dy[i]
        nx = nowX + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        if visited[ny][nx] == 1: continue
        visited[ny][nx] = 1
        board[ny][nx] = board[nowY][nowX] + 1
        q.append((ny, nx))

if check == False:
    print(-1)