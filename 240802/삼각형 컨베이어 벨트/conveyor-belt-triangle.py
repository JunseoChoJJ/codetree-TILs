n, t = map(int, input().split())
belt=[]

for _ in range(3):
    belt.append(list(map(int, input().split())))


for _ in range(t):

    tmp1 = belt[0][n-1]
    tmp2 = belt[1][n-1]
    tmp3 = belt[2][n-1]
    
    for i in range(n-1, 0, -1):
        belt[0][i] = belt[0][i-1] 
        belt[1][i] = belt[1][i-1]
        belt[2][i] = belt[2][i-1]
    belt[1][0] = tmp1
    belt[2][0] = tmp2
    belt[0][0] = tmp3
for i in range(3):
    for j in range(n):
        print(belt[i][j], end = ' ')

    print()