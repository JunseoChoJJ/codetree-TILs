n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort()

cnt = 0
for i in range(n):
    if a_list[i] != b_list[i]:
        print("No")
        cnt += 1
        break
if cnt == 0:
    print("Yes")