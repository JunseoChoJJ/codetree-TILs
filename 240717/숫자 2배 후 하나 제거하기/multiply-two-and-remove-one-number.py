import sys
n = int(input())
n_list = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n):
    n_list[i] *= 2
    
    for j in range(n):
        remain = []

        for k in range(n):
            if k != j:
                remain.append(n_list[k])        
        sum_diff = 0
        for k in range(n-2):
            sum_diff += abs(remain[k+1] - remain[k])
        
        ans = min(ans, sum_diff)
    n_list[i] //= 2


print(ans)