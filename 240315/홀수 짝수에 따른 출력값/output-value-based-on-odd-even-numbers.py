n = int(input())

def odd(n):
    if n == 1:
        return 1
    
    return odd(n - 2) + n

def even(n):
    if n == 0:
        return 0
    return even(n - 2) + n


if n % 2 == 0:
    print(even(n))
else:
    print(odd(n))