string = list(input())


di = dict()

for char in string:
    if char not in di:
        di[char] = 1
    else:
        di[char] += 1


check = False
ans = []
for key, value in di.items():
    if value == 1:
        ans.append(key)
        check = True

ans.sort()

if check == False:
    print("None")
else:
    print(ans[0])