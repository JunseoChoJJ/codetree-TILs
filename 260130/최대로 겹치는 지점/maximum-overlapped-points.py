n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

line = [0] * 101

# Please write your code here.
for i in range(n):
    first = segments[i][0]
    second = segments[i][1]


    for j in range(first, second+1):
        line[j] += 1

print(max(line))

