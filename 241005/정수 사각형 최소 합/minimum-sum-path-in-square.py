n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


# initialize
dp = [[0] * n for _ in range(n)]

dp[0][n-1] = board[0][n-1]

for i in range(n-2,-1,-1):
    dp[0][i] = dp[0][i+1] + board[0][i]
for i in range(n-1):
    dp[i+1][n-1] = dp[i][n-1] + board[i+1][n-1]

for i in range(1, n):
    for j in range(n-2,-1,-1):
        dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + board[i][j]

print(dp[n-1][0])