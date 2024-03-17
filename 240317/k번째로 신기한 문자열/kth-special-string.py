n,k,t = map(str, input().split())

n = int(n)
k = int(k)
t_num = len(t)
p_list = []

for _ in range(n):
    string = input()
    if string[0:t_num] == t:
        p_list.append(string)
p_list.sort()
print(p_list[k-1])