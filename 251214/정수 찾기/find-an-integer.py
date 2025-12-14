n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.
s1 = set(a)


for num in b:
    if num in s1:
        print(1)
    else:
        print(0)