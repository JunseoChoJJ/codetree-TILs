y = int(input())


def check(y):
    if y % 4 != 0:
        return False
    if y % 100 == 0 and y % 400 != 0:
        return False
    return True
if check(y):
    print("true")
else:
    print("false")