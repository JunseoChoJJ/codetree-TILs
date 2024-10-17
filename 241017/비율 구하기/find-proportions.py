from sortedcontainers import SortedDict
n = int(input())

sd = SortedDict()

for _ in range(n):
    color = input()

    if color not in sd:
        sd[color] = 1
    else:
        sd[color] += 1

for key, value in sd.items():
    per = value / n * 100


    print(f"{key} {per:.4f}")