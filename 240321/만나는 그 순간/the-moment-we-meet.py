n, m = map(int, input().split())

n_list = []
m_list = []

total = 0
for i in range(n):
    d, t = map(str, input().split())
    t = int(t)
    
    if d == "R":
        c = 0
        while True:
            if c == t:
                break
            c += 1
            total += 1
            n_list.append(total)
    else:
        c = 0
        while True:
            if c == t:
                break
            c += 1
            total -= 1
            n_list.append(total)
total = 0
for j in range(m):
    d, t = map(str, input().split())
    t = int(t)
    
    if d == "R":
        c = 0
        while True:
            if c == t:
                break
            c += 1
            total += 1
            m_list.append(total)
    else:
        c = 0
        while True:
            if c == t:
                break
            c += 1
            total -= 1
            m_list.append(total)
ans = 0
for i in range(len(n_list)):
    if n_list[i] == m_list[i]:
        ans = i+1
        break
if ans == 0:
    print(-1)
else:
    print(ans)