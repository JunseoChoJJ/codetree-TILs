ny, nx = 0, 0
direction = 3
dy = [1,0,-1,0]
dx = [0,-1,0,1]

string = input()

for s in string:
    if s == "R":
       direction = (direction + 1) % 4  
    elif s == "L":
        direction = (direction + 3) % 4
    else:
        ny += dy[direction]
        nx += dx[direction]

print(ny, nx)