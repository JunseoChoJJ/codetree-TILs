import sys
n_list = list(map(int, input().split()))

def diff(sum1, sum2, sum3):
    return abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

ans = sys.maxsize

for i in range(5):
    for j in range(i+1, 5):
        
        for k in range(5):
            for l in range(k+1, 5):
                if i == k or i == l or j == k or j == l: continue
                sum1 = n_list[i] + n_list[j]
                sum2 = n_list[k] + n_list[l]
                sum3 = sum(n_list) - sum1 - sum2
                if sum1 == sum2 or sum2 == sum3 or sum1 == sum3: continue
                ans = min(ans, diff(sum1, sum2, sum3))
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)