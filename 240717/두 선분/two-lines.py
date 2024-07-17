n_list = list(map(int, input().split()))

line = [0] * 101

x1 = n_list[0]
x2 = n_list[1]
x3 = n_list[2]
x4 = n_list[3]

check = False
for i in range(x1, x2+1):
    line[i] = 1

for j in range(x3, x4+1):
    if line[j] == 1:
        check = True
        break

if check == True:
    print("intersecting")
else:
    print("nonintersecting")