n = int(input())

n_list = list(map(int, input().split()))

n_list = sorted(n_list)


first = n_list[n-1] * n_list[n-2] * n_list[n-3]
second = n_list[0] * n_list[1] * n_list[n-1]



print(max(first, second))