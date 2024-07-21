n = int(input())

check = [0, 0]

ans = 0
prev_winner = 2
# 둘 다 이겼으면 2, a가 이겼으면 0, b가 이겼으면 1
for _ in range(n):
    c, s = map(str, input().split())
    s = int(s)

    if s == 0: continue
    if c == 'A':
        check[0] += s
    else:
        check[1] += s
    
    if check[0] == check[1]:
        winner = 2
    elif check[0] > check[1]:
        winner = 0
    else:
        winner = 1
    if prev_winner != winner:
        ans += 1
    
    prev_winner = winner
print(ans)