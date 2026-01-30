N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
cnt = 1
ans = 1

def checkSign(num):
    if num > 0:
        sign = "+"
    else:
        sign = "-"
    return sign



for i in range(1, N):

    sign1 = checkSign(arr[i-1])
    sign2 = checkSign(arr[i])

    if sign1 != sign2:
        cnt = 1
    else:
        cnt += 1
    ans = max(ans, cnt)
    
print(ans)

        