N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.


startX = 0
startY = 0

dxs = [1,0,-1,0]
dys = [0,-1,0,1]

mapper = {
    "E": 0,
    "S": 1,
    "W": 2,
    "N": 3
}

cnt = 0
check = False
for i in range(N):
    di = dir[i]
    dis = dist[i]
    
    direction = mapper[di]

    for j in range(dis):
        nx = startX + dxs[direction]
        ny = startY + dys[direction]

        if nx == 0 and ny == 0:
            cnt += 1
            check = True
            break
        cnt += 1
        startX = nx
        startY = ny
    if check == True:
        break

if check == False:
    print(-1)
else:
    print(cnt)