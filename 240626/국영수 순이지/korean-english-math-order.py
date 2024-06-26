class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
students = []
n = int(input())

for _ in range(n):
    string = list(map(str, input().split()))
    students.append(Student(string[0], int(string[1]), int(string[2]), int(string[3])))

students.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

for i in range(n):
    print(students[i].name, students[i].kor, students[i].eng, students[i].math )