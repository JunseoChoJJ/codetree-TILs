n, m = map(int, input().split())
n_list = list(map(int, input().split()))


def binary_search(a, b):
    cnt = 0

    for num in n_list:
        left = a
        right = b
        
        if num > right or num < left: continue
        
        while left <= right:
            mid = (left + right) // 2    

            if mid == num:
                cnt += 1
                break
            if mid > num:
                right = mid - 1
            else:
                left = mid + 1 
    
    return cnt


for _ in range(m):
    a, b = map(int, input().split())
    print(binary_search(a,b))