from sortedcontainers import SortedDict
n = int(input())

sd = SortedDict()

for _ in range(n):
    command = list(map(str, input().split()))

    if command[0] == "add":
        key = int(command[1])
        value = int(command[2])
        sd[key] = value
    elif command[0] == "find":
        key = int(command[1])
        if key in sd:
            print(sd[key])
        else:
            print("None")

    elif command[0]== "remove":
        key = int(command[1])
        del sd[key]
    else:
        if len(sd) == 0:
            print("None")
        else:
            for key, value in sd.items():
                print(value, end = ' ')
        print()