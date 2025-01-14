n = int(input())
arr = list(map(int, input().split()))

# Write your code here!


# ans variable
cost = 0
cnt = 0

while True:


    if cnt == n-1:
        break
    arr.sort()
    first = arr[0]
    second = arr[1]
    

    total = first + second

    cost += total
    arr = arr[2:]
    arr.append(total)
    cnt+= 1

print(cost)

