N = input()

# Please write your code here.
num = 0
for i in range(len(N)):
    num = num * 2 + int(N[i])

num *= 17
digit = []
while True:
    if num < 2:
        digit.append(num % 2)
        break

    digit.append(num % 2)
    num = num // 2


for num in digit[::-1]:
    print(num, end="")