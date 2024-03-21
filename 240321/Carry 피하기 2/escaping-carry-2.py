n = int(input())
n_list = []

for _ in range(n):
    n_list.append(int(input()))

ans = -1

def check(n1, n2, n3):
    if (n1 % 10 + n2 % 10 + n3 % 10) > 9:
        return False
    if n1 == 0 and n2 == 0 and n3 == 0:
        return True
    return check(n1 // 10, n2 //10, n3 // 10)

for i in range(n):
    
    for j in range(i+1, n):
        for k in range(j+1, n):
            if check(n_list[i],n_list[j], n_list[k]):
                total = n_list[i] + n_list[j] + n_list[k]
                ans = max(ans, total)

print(ans)