class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students = []
n = int(input())

for _ in range(n):
    string = list(map(str, input().split()))
    students.append(Student(string[0], string[1], string[2]))


students.sort(key=lambda x: x.height)

for student in students:
    print(student.name, student.height, student.weight)