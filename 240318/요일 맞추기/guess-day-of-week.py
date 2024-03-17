m1,d1,m2,d2 = map(int, input().split())

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

total1 = 0
total2 = 0
for i in range(m1):
    total1 += num_days[i]
total1 += d1
for i in range(m2): 
    total2 += num_days[i]
total2 += d2

if total1 <= total2:
    num = total2 - total1
    ans = num % 7
    print(days[ans])
else:
    num = total2 - total1
    ans = num % 7
    print(days[ans])