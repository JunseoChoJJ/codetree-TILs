n = int(input())

def rec(n):
    if n < 10:
        return n * n

    return rec(n // 10) + (n % 10)**2
print(rec(n))