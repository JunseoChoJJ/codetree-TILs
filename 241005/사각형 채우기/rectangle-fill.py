#top down 방식으로도 풀어보기
n = int(input())
dp = [0] * (1001)
MOD = 10007



dp[0] = 1
dp[1] = 1




for i in range(2, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD


print(dp[n])