n = int(input())

check = [0, 0, 0]

ans = 0
prev_winner = 6
# 세명 다 이겼으면 6, a가 이겼으면 0, b가 이겼으면 1, c가 이겼으면 2, a,b가 이김 3, a,c가 이김 4, b,c가 이김 5
for _ in range(n):
    c, s = map(str, input().split())
    s = int(s)

    if s == 0: continue
    if c == 'A':
        check[0] += s
    elif c == 'B':
        check[1] += s
    else:
        check[2] += s

    if check[0] == check[1] == check[2]:
        winner = 6
    elif check[0] > check[1] and check[0] > check[2]:
        winner = 0
    elif check[1] > check[0] and check[1] > check[2]:
        winner = 1
    elif check[2] > check[0] and check[2] > check[1]:
        winner = 2
    elif check[0] == check[1] and check[0] > check[2]:
        winner = 3
    elif check[0] == check[2] and check[0] > check[1]:
        winner = 4
    else:
        winner = 5
    if prev_winner != winner:
        ans += 1
    
    prev_winner = winner
print(ans)