n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
d = {}

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

big = 0
for num in d:
    
    if d[num] > big:
        big = d[num]

print(big)