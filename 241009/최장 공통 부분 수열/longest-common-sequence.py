a = list(input())
b = list(input())

lengthA = len(a)
lengthB = len(b)
dp = [[0] * lengthA for _ in range(lengthB)]


def initialize():
    if a[0] == b[0]:
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    
    for i in range(1, lengthB):
        if a[0] == b[i]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]

    for j in range(1, lengthA):
        if a[j] == b[0]:
            dp[0][j] = 1
        else:
            dp[0][j] = dp[0][j-1]

initialize()



for i in range(1, lengthB):
    for j in range(1, lengthA):
        if b[i] == a[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[lengthB-1][lengthA-1])