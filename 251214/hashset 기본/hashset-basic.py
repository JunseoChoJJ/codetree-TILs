n = int(input())

s = set()
for _ in range(n):
    cmd, val = input().split()

    if cmd == "find":
        if val in s:
            print("true")
        else:
            print("false")
    elif cmd == "add":
        s.add(val)
    else:
        s.remove(val)

# Please write your code here.
