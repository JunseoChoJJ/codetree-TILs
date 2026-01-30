n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

line = [0] * 2001
offset = 1000
for i in range(n):
    xi = x[i]
    di = dir[i]

    for j in range(1, xi+1):
        if di == "R":
            offset + j
            line[offset] += 1
        else:
            offset - j
            line[offset] += 1

cnt=0
for num in line:
    if num >= 2:
        cnt += 1

print(cnt)

    