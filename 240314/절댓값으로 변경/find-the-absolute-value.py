n = int(input())

_list = list(map(int, input().split()))

def check(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = abs(arr[i])
  


check(_list)

for elem in _list:
    print(elem, end = " ")