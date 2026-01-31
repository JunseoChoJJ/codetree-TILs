n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

dx = [0,1,-1,0]
dy = [1,0,0,-1]

mapper = {
    "R": 0,
    "D": 1,
    "U": 2,
    "L": 3
}

direction = mapper[d]

for i in range(t):
    nx = r + dx[direction]
    ny = c + dy[direction]

    if nx < 1 or ny < 1 or nx >= n or ny >= n:
        direction = 3 - direction
    else:
        r = nx
        c = ny

print(r, c)
    