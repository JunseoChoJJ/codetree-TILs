N = int(input())
a = input()
b = input()

# Write your code here!
check = False
cnt = 0
for i in range(N):

    if a[i] != b[i]:
        
        if check == False:
            cnt += 1
        check = True
    else:
        check = False

print(cnt)