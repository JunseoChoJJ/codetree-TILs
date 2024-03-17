m1,d1,m2,d2 = map(int, input().split())
string = input()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
num_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

total1 = 0
total2 = 0
for i in range(m1):
    total1 += num_days[i]
total1 += d1
for i in range(m2): 
    total2 += num_days[i]
total2 += d2

for i in range(7):
    if days[i] == string:
        check = i

cnt = 0
num = total2 - total1
day_left = num % 7
day = num // 7
cnt += day

if check >= day_left:
    cnt += 1
print(cnt)