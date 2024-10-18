from sortedcontainers import SortedSet
s = SortedSet()

n = int(input())



for _ in range(n):
    command = list(map(str, input().split(" ")))
    
    if command[0] == "add":
        x = command[1]
        s.add(x)
    elif command[0] == "remove":
        x = command[1]
        s.remove(x)
    elif command[0] == "find":
        x = command[1]
        if x in s:
            print("true")
        else:
            print("false")
    elif command[0] == "lower_bound":
        x = command[1]
        idx = s.bisect_left(x)
        if idx < len(s):
            print(s[idx])
        else:
            print("None")
            
    elif command[0] == "upper_bound":
        x = command[1]
        idx = s.bisect_right(x)
        if idx < len(s):
            print(s[idx])
        else:
            print("None")
            
    elif command[0] == "largest":
        if not s:
            print("None")
        else:
            print(s[-1])
    else:
        if not s:
            print("None")
        else:
            print(s[0])