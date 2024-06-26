class Check:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second



string = list(map(str, input().split()))
hi = Check(string[0], string[1], string[2])


print("code : " + hi.code)
print("color : " + hi.color)
print("second : " + hi.second)