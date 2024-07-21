n_list = list(map(int, input().split()))


def check(n_list):
    if n_list[1] - n_list[0] == 1 and n_list[2] - n_list[1] == 1:
        return True
    else:
        return False

cnt = 0
if check(n_list) == True:
    print(cnt)


first = abs(n_list[0] - n_list[1])
second = abs(n_list[2] - n_list[1])
print(second - 1)