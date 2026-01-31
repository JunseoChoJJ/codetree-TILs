commands = input()

# Please write your code here.

dxs = [1,0,-1,0]
dys = [0,-1,0,1]

direction = 3
startX = 0
startY = 0

time = 0
for com in commands:
    if com == "L":
        direction = (direction -1 + 4) % 4
        time += 1
    elif com == "R":
        direction = (direction + 1) % 4
        time += 1
    else:
        startX += dxs[direction]
        startY += dys[direction]
        time += 1

    if startX == 0 and startY == 0:
        check = True
        break

if check == False:
    print(-1)
else:
    print(time)