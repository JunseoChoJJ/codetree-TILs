n = int(input())
zenga=[]

for _ in range(n):
    zenga.append(int(input()))

s1,e1=map(int, input().split())
s2,e2=map(int, input().split())

tmp1 = []
tmp2 = [] 

for i in range(len(zenga)):
    
    if i >= (s1 - 1) and i <= (e1-1): continue
    tmp1.append(zenga[i])

zenga = tmp1


for j in range(len(zenga)):
    if j >= (s2-1) and j <= (e2-1): continue
    tmp2.append(zenga[j])
zenga=tmp2
print(len(zenga))
for num in zenga:
    print(num)