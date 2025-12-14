n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

# Please write your code here.

set1 = set(arr1)



for num in arr2:
    if num in set1:
        print(1, end = " ")
    else:
        print(0, end = " ")