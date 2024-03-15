n = int(input())


def check1(n):
    if n == 0:
        return
    check1(n - 1)
    print(n, end = " ")


def check2(n):
    if n == 0:
        return
    print(n, end = " ")
    check1(n - 1)

check1(n)
print()
check2(n)