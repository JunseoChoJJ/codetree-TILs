n = int(input())
pigeon_list = [-1] * 11

cnt = 0
for _ in range(n):
    pigeon, location = map(int, input().split())

    if pigeon_list[pigeon] == -1:
        pigeon_list[pigeon] = location
    else:
        if pigeon_list[pigeon] != location:
            pigeon_list[pigeon] = location
            cnt += 1
print(cnt)