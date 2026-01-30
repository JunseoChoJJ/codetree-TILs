N, B = map(int, input().split())

# Please write your code here.

digit = []
while True:

    if N < B:
        digit.append(N % B)
        break

    digit.append(N % B)
    N = N // B


for num in digit[::-1]:
    print(num, end="")