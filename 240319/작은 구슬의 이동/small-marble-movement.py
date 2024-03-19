n, t = map(int, input().split())
r,c,d = map(str, input().split())
r = int(r)
c = int(c)
board = [[1] * n for _ in range(n + 1)]

direction = 0
if d == "U":
    direction = 2
elif d == "D":
    direction = 1
elif d == "R":
    direction = 0
else:
    direction = 3
dy = [0, 1, -1, 0]
dx = [1,0, 0, -1]
time = 0


while True:
    if time == t: 
        break

    r += dy[direction]
    c += dx[direction]
    if r < 1 or c < 1 or r >= (n + 1) or c >= (n + 1):
        direction = 3 - direction
        r += dy[direction]
        c += dx[direction]
    time += 1

print(r, c)