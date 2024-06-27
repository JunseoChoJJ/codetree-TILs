n = int(input())

n_list = [0] * (201)

for _ in range(n):
    a, b = map(int, input().split())
    a += 100
    b += 100
    
    for i in range(a, b):
        n_list[i] += 1

print(max(n_list))