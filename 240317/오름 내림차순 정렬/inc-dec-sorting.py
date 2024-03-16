n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()
for elem in n_list:
    print(elem, end = " ")
print()
n_list = n_list[::-1]
for elem in n_list:
    print(elem, end = " ")