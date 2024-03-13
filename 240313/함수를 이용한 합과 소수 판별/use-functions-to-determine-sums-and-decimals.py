a, b = map(int, input().split())

def check2(num):
    if (num % 10 + num // 10) % 2 == 0:
        return True
    else:
        return False

def check(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return True
cnt = 0

for i in range(a, b+1):
    if check(i) and check2(i):
        cnt += 1
print(cnt)