from sortedcontainers import SortedDict
n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
d = {}
sd = SortedDict()
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1


for key, value in d.items():
    percentile = f"{value / n * 100:.4f}"

    sd[key] = percentile

for key, value in sd.items():
    print(key, value)
