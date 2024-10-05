n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))



dp = [[0] * n for _ in range(n)]


dp[0][0] = board[0][0]

# initialize
for i in range(n-1):
    dp[0][i+1] = board[0][i+1] + dp[0][i]

    dp[i+1][0] = board[i+1][0] + dp[i][0]


for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + board[i][j]



ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])
print(ans)