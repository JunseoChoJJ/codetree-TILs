n = int(input())
n_list = []

for _ in range(n):
    x, y = map(int, input().split())

    n_list.append((x, y))

ans = float("inf")
for i in range(n):

    for j in range(i + 1, n):

        x = abs(n_list[i][0] - n_list[j][0])
        y = abs(n_list[i][1] - n_list[j][1])
        total = x * x + y * y
        ans = min(ans, total)

print(ans)