n = int(input())


left = 1
right = 2 * n


def isPossible(maxSum):

    three = maxSum // 3
    five = maxSum // 5
    common = maxSum // 15

    total = three + five - common

    return maxSum - total

while left <= right:
    mid = (left + right) // 2

    if isPossible(mid) == n:
        print(mid)
        break
    
    if isPossible(mid) < n:
        left = mid + 1
    else:
        right = mid - 1