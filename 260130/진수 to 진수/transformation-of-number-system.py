a, b = map(int, input().split())
n = input()

# Please write your code here.

num = 0
for i in range(len(n)):
    num = num * a + int(n[i])

digit = []
while True:
    if num < b:
        digit.append(num % b)
        break

    digit.append(num % b)
    num = num // b

for num in digit[::-1]:
    print(num, end="")