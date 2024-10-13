n = int(input())

length = n // 5

minCoin = 100000


while True:
    if length == -1:
        break

    remain = n - length * 5
    if remain % 2 == 0:
        minCoin = min(minCoin, length + remain // 2)


    length -= 1

if minCoin == 100000:
    print(-1)
else:
    print(minCoin)