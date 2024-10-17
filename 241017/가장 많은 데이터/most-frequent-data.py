n = int(input())

string = dict()

ans = 0
for _ in range(n):
    word = input()

    if word in string:
        string[word] += 1 
    else:
        string[word] = 1
    ans = max(ans, string[word])

print(ans)