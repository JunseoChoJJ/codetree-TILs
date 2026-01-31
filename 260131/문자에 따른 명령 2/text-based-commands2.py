dirs = input()

# Please write your code here.
dx = [1,0,-1,0]
dy = [0,-1,0,1]


x, y = 0,0
dirNum = 3

for dir in dirs:
    if dir == "R":
        dirNum = (dirNum + 1) % 4
    elif dir == "L":
        dirNum = (dirNum -1 + 4) % 4
    else:
        x += dx[dirNum] 
        y += dy[dirNum]

print(x, y)