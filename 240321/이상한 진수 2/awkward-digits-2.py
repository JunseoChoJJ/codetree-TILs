string = list(input())
ans = 0

def check(string):
    num = 0
    string = string[::-1]
    for i in range(len(string)):
        if string[i] == '1':
            if len(string) != 1:
                num += 2**i 
    return num

for i in range(len(string)):
    if string[i] == '0':
        string[i] = '1'
        num = check(string)
        ans = max(ans, num)
        string[i] = '0'
    else:
        num = check(string)
        ans = max(ans, num)
print(ans)