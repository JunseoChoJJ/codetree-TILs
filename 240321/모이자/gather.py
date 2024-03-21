import sys
n = int(input())
n_list = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(n):
    dis = 0
    for j in range(n):
        distance = abs(j-i)
        dis += distance * n_list[j]
    min_val = min(dis, min_val)

print(min_val)