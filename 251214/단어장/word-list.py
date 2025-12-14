from sortedcontainers import SortedDict
n = int(input())
words = [input() for _ in range(n)]
sd = SortedDict()
# Please write your code here.
for word in words:
    if word in sd:
        sd[word] += 1
    else:
        sd[word] = 1

for key, value in sd.items():
    print(key, value)