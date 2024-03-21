string = list(input())


cnt = 0
for i in range(len(string)):
    if string[i] == "(" and string[i-1] == "(":
        for j in range(i+2, len(string)):
            if string[j] == ")" and string[j-1] == ")":
                cnt += 1
print(cnt)