class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())
people = []

for _ in range(n):
    string = list(map(str, input().split()))
    people.append(Person(string[0], int(string[1]), int(string[2])))


people.sort(key=lambda x: (x.h, -x.w))

for person in people:
    print(person.name, person.h, person.w)