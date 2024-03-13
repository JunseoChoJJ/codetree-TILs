a,b = map(int, input().split())

def prime(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return True

total = 0
if a == b:
    return 0
for i in range(a, b + 1):
    if prime(i):
        total += i
    else:
        continue
print(total)