a,b,x,y = map(int, input().split())

first = b-a
second = abs(a-x) + abs(y-b)
third = abs(a-y) + abs(x-b)

print(min(first, second, third))