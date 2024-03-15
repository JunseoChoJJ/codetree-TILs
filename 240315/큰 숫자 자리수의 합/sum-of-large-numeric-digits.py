a,b,c = map(int, input().split())

num = a * b * c

def check(num):
    if num < 10:
        return num
    return check(num // 10) + num % 10

print(check(num))