n = int(input())
n_list = []

for _ in range(n):
    n_list.append(int(input()))

cnt = 0 
tmp = []
for i in range(n):
    if i == 0 or n_list[i] * n_list[i-1] < 0:
        tmp.append(cnt)
        cnt = 1
    else:
        cnt += 1
print(max(tmp))