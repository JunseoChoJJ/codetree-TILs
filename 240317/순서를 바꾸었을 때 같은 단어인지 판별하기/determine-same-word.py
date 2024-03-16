a_list = list(input())
b_list = list(input())

a_list.sort()
b_list.sort()


def equal():
    global a_list
    global b_list

    a1 = len(a_list)
    b1 = len(b_list)

    if a1 != b1:
        return False
    else:
        num = a1
    for i in range(num):
        if a_list[i] != b_list[i]:
            return False
    return True

if equal():
    print("Yes")
else:
    print("No")