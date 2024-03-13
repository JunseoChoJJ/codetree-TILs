a, b = map(int, input().split())

cnt = 0

def check(num):
    global cnt
    if num % 3 == 0 or check2(num):
        cnt += 1
        

def check2(num):
    n = list(str(num))
    n2 = list(map(int, n))
    for a in range(len(n2)):
        if n2[a] == 3 or n2[a] == 6 or n2[a] == 9:
            return True
for i in range(a, b + 1):
    check(i)
print(cnt)