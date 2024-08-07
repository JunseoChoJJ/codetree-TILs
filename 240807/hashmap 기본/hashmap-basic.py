n = int(input())
d = dict()

for _ in range(n):
    command = list(input().split(" "))

    if command[0] == "add":
        k = command[1]
        v = command[2]
        d[k] = v

    elif command[0] == "find":
        k = command[1]

        if k in d:
            print(d[k])
        else:
            print("None")

    else:
        k = command[1]
        d.pop(k)