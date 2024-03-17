a,b,c = map(int, input().split())

day = 11
hour = 11
mins = 11
time = 0

while True:
    if day > a:
        time = -1
        break
    if day == a and hour > b:
        time = -1 
        break
    if day == a and hour == b and mins > c:
        time = -1
        break
    if day == a and hour == b and mins == c:
        break

    time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins = 0
    
    if hour == 24 and mins == 0:
        day += 1
        hour = 0
        mins = 0

print(time)