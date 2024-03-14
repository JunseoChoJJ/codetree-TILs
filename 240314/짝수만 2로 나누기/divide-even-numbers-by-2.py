n = int(input())


_list = list(map(int, input().split()))


def modify(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
        else:
            continue
modify(_list)


for elem in _list:
    print(elem, end = " ")