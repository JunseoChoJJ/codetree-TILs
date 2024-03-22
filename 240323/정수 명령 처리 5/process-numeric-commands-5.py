n = int(input())

n_list = []

for _ in range(n):
    command = list(input().split())
    
    if command[0] == "push_back":
        n_list.append(int(command[1]))
    elif command[0] == "pop_back":
        n_list.pop()
    elif command[0] == "size":
        print(len(n_list))
    else:    
        print(n_list[int(command[1]) - 1])