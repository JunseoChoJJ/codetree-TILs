import sys
n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

ans = sys.maxsize
for i in range(n):
    distance = 0
    for j in range(n):
        if i == j: continue
        if i < j:
            num = j - i
        if i > j:
            num = n - i + j
        distance += n_list[j] * num

    ans = min(ans, distance)
print(ans)