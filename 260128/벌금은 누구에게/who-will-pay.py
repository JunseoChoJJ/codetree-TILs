N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

num = [0] * (N+1)

for st in student:
    num[st] += 1

    if num[st] == K:
        print(st)

        break

