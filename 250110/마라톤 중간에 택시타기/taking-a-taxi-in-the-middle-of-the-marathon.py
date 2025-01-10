n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Write your code here!


# distnace from two points
def distance(index,check):

    if check == 1:
        x1 = x[index]
        x2 = x[index+1]
        y1 = y[index]
        y2 = y[index+1]

    else:
        x1 = x[index]
        x2 = x[index-1]
        y1 = y[index]
        y2 = y[index-1]

    return abs(x2-x1) + abs(y2-y1)
# L
l = [0]
total = 0
for i in range(n-1):
    num = distance(i,1)
    total += num
    l.append(total)

r = [0]
total2 = 0
# R
for j in range(n-1,-1,-1):
    num = distance(j,0)
    total2 += num
    r.append(total2)


#main
ans = 0
for i in range(1, n-1):
    p = n - i - 2
    diff = abs(x[i+1] - x[i-1]) + abs(y[i+1] - y[i-1]) 
    value = l[i-1] + diff + r[p] 
    
    ans = max(ans, value)
print(ans)
