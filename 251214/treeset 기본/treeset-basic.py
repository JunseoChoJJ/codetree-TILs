from sortedcontainers import SortedSet
n = int(input())
command = []
x = []

sd = SortedSet()

for _ in range(n):
    line = input().split()
    
    command = line[0]
    
    
    if command == "add":
        value = int(line[1])
        sd.add(value)
    elif command == "remove":
        value = int(line[1])
        sd.remove(value)
    elif command == "find":
        value = int(line[1])
        if value in sd:
            print("true")
        else:
            print("false")
    elif command == "lower_bound":
        value = int(line[1])
        if value <= sd[-1]:
            print(sd[sd.bisect_left(value)])
        else:
            print("None")
    elif command == "upper_bound":
        
        value = int(line[1])
        if value < sd[-1]:
            print(sd[sd.bisect_right(value)])
        else:
            print("None")
    elif command == "largest":
        if len(sd) == 0:
            print("None")
        else:
            print(sd[-1])
    else:
        if len(sd) == 0:
            print("None")
        else:
            print(sd[0])


