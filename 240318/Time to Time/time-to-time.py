a,b,c,d = map(int, input().split())
hour = a
mins = b

time = 0
while True:
    if hour == c and mins == d:
        break
    time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0
    

print(time)