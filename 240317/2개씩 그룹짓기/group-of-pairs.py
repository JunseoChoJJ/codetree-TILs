n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

def common(n, n_list):
    ans = 0
    for i in range(n):
        tmp = n_list[i] + n_list[2 * n - i - 1]
        if tmp > ans:
            ans = tmp
    return(ans)

print(common(n, n_list))