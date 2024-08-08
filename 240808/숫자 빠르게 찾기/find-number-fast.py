n, m = map(int, input().split())
n_list=list(map(int, input().split()))

def binary_search(target):

    left = 0 
    right = n-1
    idx = -1
    check = False
    while left <= right:
        
        mid = (left + right) // 2

        if n_list[mid] == target:
            idx = mid 
            check = True
            break

        if n_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1 

    if check == True:
        return idx+1
    else:
        return -1


for _ in range(m):
    num = int(input())
    print(binary_search(num))