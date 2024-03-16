n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input())

n_list.sort()

for i in range(n):
    print(n_list[i])