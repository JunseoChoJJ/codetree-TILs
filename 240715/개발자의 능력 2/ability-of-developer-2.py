n_list = list(map(int, input().split()))


def get_diff(sum1, sum2):
    sum3 = sum(n_list) - sum1 - sum2
    return abs(max(sum1,sum2,sum3)- min(sum1, sum2, sum3))

ans = float("inf")
for i in range(0, 6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            for l in range(k+1, 6):
                sum1 = n_list[i] + n_list[j]
                sum2 = n_list[k] + n_list[l]
                ans = min(ans, get_diff(sum1, sum2))
                sum1 = n_list[i] + n_list[k]
                sum2 = n_list[j] + n_list[l]
                ans = min(ans, get_diff(sum1, sum2))
                sum1 = n_list[i] + n_list[l]
                sum2 = n_list[j] + n_list[k]
                ans = min(ans, get_diff(sum1, sum2))


print(ans)