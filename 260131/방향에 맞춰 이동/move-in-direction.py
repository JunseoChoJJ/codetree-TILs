n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

dx = [-1,1,0,0]
dy = [0,0,1,-1]


x, y = 0, 0

for i in range(n):
    if dir[i] == "N":
        y += dy[2] * dist[i]

    elif dir[i] == "E":
        x += dx[1] * dist[i]
    elif dir[i] == "S":
        y += dy[3] * dist[i]
    else:
        x += dx[0] * dist[i]
print(x, y)