s = int(input())
max_num = 2 * 10**9

def binary_search(target):
    left=0
    right=max_num
    min_num = max_num

    while left <= right:
        mid = (left + right) // 2

        if mid * (mid+1) // 2 > target:
            right = mid - 1
            min_num = min(min_num, mid)
        else:
            left = mid + 1
    return min_num-1

print(binary_search(s))