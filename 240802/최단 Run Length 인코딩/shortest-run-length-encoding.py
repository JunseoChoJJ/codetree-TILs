string=list(input())
n = len(string)

def check_length(a):
    run_length=''

    cnt = 1
    for i in range(len(a)):
        if i+1 == len(a):
            run_length += a[i]
            run_length += str(cnt)
            break
        if a[i] != a[i+1]:
            run_length += a[i]
            run_length += str(cnt)
            cnt = 1
        else:
            cnt+=1
    return len(run_length)


min_length=100
for i in range(n):
    length = check_length(string)
    min_length = min(min_length, length)

    tmp = string[n-1]
    for j in range(n-1, 0,-1):
        string[j] = string[j-1]
    string[0] = tmp
print(min_length)