a,b = map(int, input().split())

total = a + b
subtraction = a - b
ans = total / subtraction
num = round(ans, 2)
print(num)