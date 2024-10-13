n = int(input())
n_list = list(map(int, input().split()))

total = 0

while True:
    n_list.sort()
    if len(n_list) == 2:
        total += sum(n_list)
        break
    to = n_list[0] + n_list[1]
    total += to
    n_list = n_list[2:]
    n_list.append(to)

print(total)