s = input()



ans = 0
y,x = 0, 0
check = False

dy = [-1,0,1,0]
dx = [0,1,0,-1]

dirs = 0
for i in range(len(s)):
    if s[i] == 'F':
        y += dy[dirs]
        x += dx[dirs]
    elif s[i] == 'L':
        dirs = (dirs + 3) % 4
    else:
        dirs = (dirs + 1) % 4
    ans += 1
    if y == 0 and x == 0:
        check = True
        break
if check == False:
    print(-1)
else:
    print(ans)