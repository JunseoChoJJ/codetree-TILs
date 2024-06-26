class Student:
    def __init__(self, name, h, w):
        self.name = name
        self.h  = h
        self.w = w
students = []
for i in range(5):
    string = list(map(str, input().split()))
    students.append(Student(string[0], int(string[1]), float(string[2])))
students.sort(key=lambda x: (x.name))


print("name")
for student in students:
    print(student.name, student.h, student.w)
print("")

students.sort(key=lambda x: (-x.h))
print("height")
for student in students:
    print(student.name, student.h, student.w)