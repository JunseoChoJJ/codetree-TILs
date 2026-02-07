arr = list((input().split()))


reverse = arr[::-1]

ans = ""
for elem in reverse:
    ans += elem

print(ans)