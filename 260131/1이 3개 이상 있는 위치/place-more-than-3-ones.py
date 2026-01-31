n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs = [1,0,-1,0]
dys = [0,-1,0,1]

cnt = 0
for i in range(n):
    for j in range(n):
        check = 0
        for dx, dy in zip(dxs, dys):  
            nx = i + dx
            ny = j + dy

            if ny < 0 or nx < 0 or ny >= n or nx >=n: continue
            if grid[nx][ny] == 1:
                check += 1

        if check >= 3:
            cnt += 1

print(cnt)