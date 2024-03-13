m, d = map(int, input().split())


def check(m,d):
    if m > 12:
        return False
    if d > 31:
        return False
    if m == 2 and d > 28:
        return False
    if (m ==2 or m == 4 or m == 6 or m == 9 or m == 11) and d > 30:
        return False
    return True

if check(m, d):
    print("Yes")
else:
    print("No")