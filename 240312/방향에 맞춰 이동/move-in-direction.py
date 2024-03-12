n = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

startY = 0
startX = 0
for _ in range(n):

    direction, distance = input().split()

    dis = int(distance)

    if direction == "N":
        startY += dy[3]
        startX += dis *dx[3]
    elif direction == "S":
        startY += dy[2]
        startX += dis * dx[2]
    elif direction == "W":
        startY += dis * dy[0]
        startX += dx[0]
    else:
        startY += dis * dy[1]
        startX += dx[1]
    
print(startY, startX)