n, m = map(int, input().split())
n_list = list(map(int, input().split()))

def check(a1, a2):
    global n_list
    return sum(n_list[a1-1:a2])

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(check(a1, a2))