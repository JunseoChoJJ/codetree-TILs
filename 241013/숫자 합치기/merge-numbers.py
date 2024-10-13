n = int(input())
n_list = list(map(int, input().split()))

total = 0

while True:
    if len(n_list) == 2:
        total += n_list[0] + n_list[1]
        break
    n_list.sort()
    to = n_list[0] + n_list[1]
    total += to
    n_list = n_list[2:]
    n_list.append(to)

print(total)