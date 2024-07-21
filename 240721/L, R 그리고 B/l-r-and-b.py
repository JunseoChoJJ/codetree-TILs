from collections import deque
board = []

for _ in range(10):
    board.append(input())

board2 = [[0] * 10 for _ in range(10)]
visited = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            startY = i
            startX = j

q = deque([(startY, startX)])
board2[startY][startX] = 0
visited[startY][startX] = 1

dy = [-1,1,0,0]
dx = [0,0,-1,1]
check = False
while q:
    (nowY, nowX) = q.popleft()
    if check == True:
        break
    for i in range(4):
        ny = nowY + dy[i]
        nx = nowX + dx[i]
    
        if ny < 0 or nx < 0 or ny >= 10 or nx >= 10: continue
        if board[ny][nx] == 'B':
            print(board2[nowY][nowX])
            check = True
            break        
        if board[ny][nx] == 'R': continue
        if visited[ny][nx] == 1: continue
        visited[ny][nx] = 1
        board2[ny][nx] = board2[nowY][nowX] + 1

        q.append((ny, nx))