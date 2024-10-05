n, k = map(int, input().split())


coins=[]

for _ in range(n):
    num = int(input())
    coins.append(num)

coins.reverse()

cnt = 0

for coin in coins:
    if k // coin > 0:
        cnt += k // coin
        k = k % coin

print(cnt)