# 동일한 블록의 크기가 격자판에 놓여있을때 어떤 것이 클지도 고민해야하는 문제
n = int(input())
board=[]

for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]
dy = [0,0,-1,1]
dx = [1,-1,0,0]

cnt = 0
def dfs(y, x):
    visited[y][x] = 1
    size= board[y][x]
    global cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        if visited[ny][nx] == 1: continue
        if board[ny][nx] != size: continue
        visited[ny][nx] = 1
        cnt += 1
        dfs(ny, nx)

block=[0] * 101


block_cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt = 1
            dfs(i, j)
            if block[board[i][j]] == 0:
                block[board[i][j]] = cnt
            else:
                if cnt > block[board[i][j]]:
                    block[board[i][j]] = cnt
            if cnt >= 4:
                block_cnt += 1

max_num = 0
for i in range(101):
    if block[i] > max_num:
        max_num = block[i]

print(block_cnt, max_num)