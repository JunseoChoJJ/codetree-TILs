n, m = map(int, input().split())
n_list = list(map(int, input().split()))


def custom_bound(target):
    left = 0
    right = n-1
    max_index=-1

    while left <= right:
        mid = (left + right) // 2

        if n_list[mid] <= target:
            max_index = max(mid, max_index)
            left = mid+1
        else:
            right = mid - 1
    
    return max_index

def lower_bound(target):
    left = 0
    right = n-1
    min_index = n

    while left <= right:
        mid = (left + right) // 2

        if n_list[mid] >= target:
            min_index = min(mid, min_index)
            right=mid-1
        else:
            left=mid+1
    return min_index

for _ in range(m):
    num = int(input())
    min_index = lower_bound(num)
    max_index = custom_bound(num)

    print(max_index - min_index+1)