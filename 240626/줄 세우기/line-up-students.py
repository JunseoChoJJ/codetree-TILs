class Student:
    def __init__(self, height, weight, number):
        self.height =  height
        self.weight = weight
        self.number = number

students = []

n = int(input())
for i in range(1, n+1):
    string = list(map(int, input().split()))
    students.append(Student(string[0], string[1], i))

students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for j in range(n):
    print(students[j].height, students[j].weight, students[j].number)