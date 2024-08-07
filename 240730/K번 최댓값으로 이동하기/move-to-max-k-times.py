from collections import deque
n, k = map(int, input().split())
board=[]
for _ in range(n):
    board.append(list(map(int, input().split())))

startY, startX = map(int, input().split())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

for _ in range(k):
    
    q = deque([(startY-1, startX-1)])
    first = board[startY-1][startX-1]
    
    max_num = -1
    visited = [[0] * n for _ in range(n)]
    visited[startY-1][startX-1] = 1
    while q:
        (nowY, nowX) = q.popleft()
    
        for i in range(4):
            ny = nowY + dy[i]
            nx = nowX + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if board[ny][nx] >= first: continue
            if visited[ny][nx] == 1: continue
            visited[ny][nx] = 1
            max_num = max(max_num, board[ny][nx])
            q.append((ny, nx))
            
    if max_num == -1:
        break
    
    check2 = False
    for i in range(n): 
        if check2 == True:
            break
        for j in range(n):
            if board[i][j] == max_num and visited[i][j] == 1:
                startY = i+1
                startX = j+1
                check2 = True
                break

    
print(startY, startX)