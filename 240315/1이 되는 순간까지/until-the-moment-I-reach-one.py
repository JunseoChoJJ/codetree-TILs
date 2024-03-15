n = int(input())

def rec(n):
    if n == 1:
        return

    if n % 2 == 0:
        return rec(n // 2) + 1
    else: 
        return rec(n // 3) + 1

print(rec(n))