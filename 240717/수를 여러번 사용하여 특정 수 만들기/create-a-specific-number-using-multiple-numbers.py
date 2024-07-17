a,b,c = map(int, input().split())


check = c // b

ans = 0
for i in range(check+1):
    sum_b = b * i 
    num_a = 0
    while True:
        total = sum_b + num_a * a
        if total > c:
            total = sum_b + (num_a - 1) * a
            break
        num_a += 1
    ans = max(ans, total)
print(ans)