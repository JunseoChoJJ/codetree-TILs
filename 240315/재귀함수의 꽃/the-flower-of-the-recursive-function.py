n = int(input())


def check(n):
    if n == 0:
        return 
    print(n, end = " ")
    check(n - 1)
    print(n, end = " ")

check(n)