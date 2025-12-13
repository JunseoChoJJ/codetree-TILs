n = int(input())
commands = []
d = {}
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        d[k] = v
        commands.append((cmd, k, v))
    elif cmd == "remove":
        d.pop(k)
        commands.append((cmd, k))
    else:
        if k in d:
            print(d[k])
        else:
            print("None")

# Please write your code here.
