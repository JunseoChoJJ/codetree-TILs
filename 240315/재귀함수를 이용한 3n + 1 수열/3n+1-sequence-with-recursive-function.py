n = int(input())
cnt = 0
def check(n):
    global cnt
    if n == 1:
        return cnt
    cnt += 1
    return check(n // 2) if n % 2 == 0 else check(n * 3 + 1)
    

print(check(n))