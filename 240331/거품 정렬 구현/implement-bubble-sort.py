n = int(input())
n_list = list(map(int, input().split()))

sorted = True

while True:
    sorted = True
    for i in range(len(n_list) - 1):
        if n_list[i] > n_list[i+1]:
            tmp = n_list[i]
            n_list[i] = n_list[i+1]
            n_list[i+1] = tmp
            sorted = False
    if sorted == True:
        break

for num in n_list:
    print(num, end = " ")