n = int(input())

def check(n):
    if n == 0:
        return

    check(n - 1)
    print("*" * n)

check(n)