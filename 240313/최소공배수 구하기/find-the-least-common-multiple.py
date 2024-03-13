n, m = map(int, input().split())

if n <= m:
    small = n
else:
    small = m

for i in range(1, small + 1):
    if n % i == 0 and m % i == 0:
        common = i

n1 = n // common
m1 = m // common

print(common * n1 * m1)