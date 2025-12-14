from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()


for _ in range(n):
    line = input().split()

    if line[0] == "add":
        k = int(line[1])
        v = int(line[2])

        sd[k] = v

    elif line[0] == "remove" :
        k = int(line[1])
        sd.pop(k)
    elif line[0] == "find":
        k = int(line[1])
        if k in sd:
            print(sd[k])
        else:
            print("None")
    else:
        if sd:
            for key, value in sd.items():
                print(value, end= " ")
            print()
        else:
            print("None")

