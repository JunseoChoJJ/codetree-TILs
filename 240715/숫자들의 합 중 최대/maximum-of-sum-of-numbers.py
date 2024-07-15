x, y = map(int, input().split())

ans = 0

def digit(num):
    if num < 10:
        return num
    return digit(num // 10) + num % 10

for i in range(x, y+1):
    tmp = digit(i) 

    ans = max(ans, tmp)
print(ans)