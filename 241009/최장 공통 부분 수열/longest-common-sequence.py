a = list(input())
b = list(input())

length = len(a)

dp = [[0] * length for _ in range(length)]


def initialize():
    if a[0] == b[0]:
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    
    for i in range(1, length):
        if a[0] == b[i]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]

    for j in range(1, length):
        if a[j] == b[0]:
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j-1]

initialize()



for i in range(1, length):
    for j in range(1, length):
        if b[i] == a[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[length-1][length-1])