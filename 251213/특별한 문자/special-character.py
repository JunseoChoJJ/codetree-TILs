str = input()

# Please write your code here.
d = {}

for char in str:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

check = False

for char in d:
    if d[char] == 1:
        print(char)
        check = True
        break
if check == False:
    print("None")