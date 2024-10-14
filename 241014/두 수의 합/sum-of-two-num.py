n, k = map(int, input().split())
n_list = list(map(int, input().split()))

cnt = 0

for num in n_list:
    remain = k - num

    if remain in n_list:
        cnt += 1

print(cnt// 2)