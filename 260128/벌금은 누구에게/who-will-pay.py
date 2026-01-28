N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

num = [0] * (N+1)
check = False

for st in student:
    num[st] += 1

    if num[st] == K:
        check = True
        print(st)
        break

if check == False:
    print(-1)