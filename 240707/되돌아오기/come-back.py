n = int(input())
mapper = {
    'N': 3,
    'E': 0,
    'S': 1,
    'W': 2
}

dy = [0,1,0,-1]
dx = [1,0,-1,0]

y, x = 0, 0 
cnt = 0
check = False
for _ in range(n):
    direction, distance = tuple(input().split())

    distance = int(distance)
    dirs = mapper[direction]
    for i in range(distance):
        y = y + dy[dirs]
        x = x + dx[dirs]
        
        cnt += 1
        if y == 0 and x == 0:
            check = True
            print(cnt)
            break
    if check == True:
        break
if check == False:
    print(-1)