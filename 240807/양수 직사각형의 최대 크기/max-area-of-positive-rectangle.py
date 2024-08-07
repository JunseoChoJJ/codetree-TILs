n, m = map(int, input().split())
board=[]

for _ in range(n):
    board.append(list(map(int, input().split())))

max_cnt = 0
for i in range(n):
    for j in range(m):
        
        cnt = 0
        for k in range(i, n):
            for l in range(j, m):
                if board[k][l] > 0:
                    cnt += 1
        max_cnt = max(max_cnt, cnt)

print(max_cnt)