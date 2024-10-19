from sortedcontainers import SortedSet



t = int(input())


for _ in range(t):
    s = SortedSet()
    k = int(input())
    for _ in range(k):
        command = list(map(str, input().split()))
        
        n = int(command[1])
        if command[0] == 'I':
            s.add(n)

        elif command[0] == 'D':
            if n == 1:
                if not s:
                    continue
                else:
                    big = s[-1]
                    s.remove(big)
            else:
                if not s:
                    continue
                else:
                    small = s[0]
                    s.remove(small)

    if s:
        print(s[-1], s[0])

    else:
        print("EMPTY")