n = int(input())

n_list = [0] * 101

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        n_list[i] += 1

print(max(n_list))