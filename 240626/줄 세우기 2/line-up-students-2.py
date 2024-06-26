class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

students=[]
n = int(input())
for i in range(1, n+1):
    string = list(map(int, input().split()))
    students.append(Student(string[0], string[1], i))


students.sort(key=lambda x: (x.h, -x.w))

for student in students:
    print(student.h, student.w, student.num)