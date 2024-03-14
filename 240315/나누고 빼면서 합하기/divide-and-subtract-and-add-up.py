n, m = map(int, input().split())
n_list = list(map(int, input().split()))

def check(n, m, n_list):
    
    total = n_list[m-1]
    
    while True:
        if m == 1:
            break
        if m % 2 == 0:
            m //= 2
            total += n_list[m-1]
        else:
            m -= 1
            total += n_list[m-1]
    return total


print(check(n, m, n_list))