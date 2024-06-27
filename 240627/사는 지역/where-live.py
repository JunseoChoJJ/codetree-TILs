class Info:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

n = int(input())
users = []

for _ in range(n):
    string = list(map(str, input().split()))
    users.append(Info(string[0], string[1], string[2]))


users.sort(key=lambda x: x.name)

print(f"name {users[n-1].name}")
print(f"addr {users[n-1].addr}")
print(f"city {users[n-1].city}")