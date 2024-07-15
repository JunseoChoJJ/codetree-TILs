n = int(input())
n_list = list(map(int, input().split()))

cnt = 0


for i in range(1, n + 1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(i - n_list[0]) <= 2 or abs(j - n_list[1]) <= 2 or abs(k - n_list[2]) <= 2:
                cnt += 1
print(cnt)