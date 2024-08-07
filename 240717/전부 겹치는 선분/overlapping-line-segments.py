# O(n^2)이 아니라 O(n)으로 풀어야 함
check = [0] * 101
n = int(input())

for _ in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1, x2+1):
        check[j] += 1

ans = False
for i in range(101):
    if check[i] == n:
        ans = True
        break

if ans == False:
    print("No")
else:
    print("Yes")