n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

block = [0] * (n+1)

for i in range(k):
    first = commands[i][0]
    second = commands[i][1]

    for j in range(first, second + 1):
        block[j] += 1
print(max(block))