n, m = map(int, input().split())
n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))



def binary_search(target):

    left = 0 
    right = n-1
    min_idx = n

    while left <= right:
        mid = (left + right) // 2
        
        if n_list[mid] >= target:
            min_idx = min(min_idx, mid)
            right = mid-1
            
        else:
            left = mid + 1
            
    return min_idx

for m in m_list:
    index = binary_search(m)
    if n_list[index] == m:
        print(index + 1)
    else:
        print(-1)