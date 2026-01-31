n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.



# choose start position
check = k // n

if check == 0:
    startX = 0
    startY = k-1
    dir = "D"
elif check == 1:
    startX = k -n - 1
    startY = n-1 
    dir = "L"
elif check == 2:
    startX = n-1
    startY = 3 * n -k
    dir = "U"
else:
    startX = 4 * n - k
    startY = 0
    dir = "R"

#R,U,D,L
dxs = [0,-1,1,0]
dys = [1,0,0,-1]

mapper = {
    "R": 0,
    "U": 1,
    "D": 2,
    "L": 3

}

cnt = 1
# main
while True:
    mirror = grid[startX][startY]
    if dir == "D":
        if mirror == "/":
            dir = "L"
        else:
            dir = "R"
    elif dir == "L":
        if mirror == "/":
            dir = "D"
        else:
            dir = "U"
    elif dir == "U":
        if mirror == "/":
            dir = "R"
        else:
            dir = "L"
    else:
        if mirror == "/":
            dir = "U"
        else:
            dir = "D"
    di = mapper[dir]
    nx = startX + dxs[di]
    ny = startY + dys[di]

    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        print(cnt)
        break

    cnt += 1
    startX = nx
    startY = ny

