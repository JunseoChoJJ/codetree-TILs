s = list(input())

def check(s):
    character = s[0]
    for i in range(len(s)):
        if character != s[i]:
            return True
    return False
    


if check(s):
    print("Yes")
else:
    print("No")