n = int(input())

n_list = list(map(int, input().split()))

n_sort = sorted(n_list)


check = n_sort[0]
quick = False

for i in range(n):
    if n_sort[i] !=  check:
        quick = True
        ans = n_sort[i]
        break

if quick == False:
    print(-1)
cnt = 0

for j in range(n):
    if n_list[j] == ans:
        hi = j
        cnt+=1



if cnt == 1:
    print(hi+1)
else:
    print(-1)