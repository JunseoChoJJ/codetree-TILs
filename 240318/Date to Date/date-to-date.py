m1,d1,m2,d2 = map(int, input().split())

ans = 1
month = m1
day = d1

num_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    if month == m2 and day == d2:
        break
    
    ans += 1
    day += 1

    if day > num_days[month]:
        month += 1
        day = 0
    
print(ans)