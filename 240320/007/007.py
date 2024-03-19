string = input().split()

class People:
    def __init__(self, code, point, time):
        self.c = code
        self.p = point
        self.t = time

people1 = People(string[0],string[1],string[2])


print("secret code : " + people1.c)
print("meeting point : " + people1.p)
print("time : " + people1.t)