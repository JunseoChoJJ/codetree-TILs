n, k = map(int, input().split())

n_list = [0] * (n+1)

for _ in range(k):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        n_list[j] += 1

print(max(n_list))