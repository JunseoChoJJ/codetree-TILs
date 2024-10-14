n = int(input())
nList = []

for _ in range(n):
    character = input()
    character = ''.join(sorted(character))
    nList.append(character)



count = dict()


for char in nList:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

ans =[]
for val in count.values():
    ans.append(val)

print(max(ans))