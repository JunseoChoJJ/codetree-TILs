class Expect:
    def __init__(self, date,day, weather):
        self.date =date
        self.day = day
        self.weather = weather

check = []

n = int(input())
for _ in range(n):
    string = list(map(str, input().split()))
    check.append(Expect(string[0], string[1], string[2]))

check.sort(key=lambda x:x.date)

target_idx = 0
for i, c in enumerate(check):
    if c.weather == "Rain":
        target_idx = i
        break

print(check[target_idx].date, check[target_idx].day, check[target_idx].weather)