a, b = map(int, input().split())


def check(a, b):
    if a > b:
        b += 10
        a *= 2
    else:
        a += 10
        b *= 2
    return a, b


a, b = check(a, b)
print(a, b)