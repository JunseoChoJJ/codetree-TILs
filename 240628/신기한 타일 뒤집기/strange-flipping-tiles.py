n = int(input())

offset = 100000

n_list = [0] * 200001

for _ in range(n):
    distance, direction = map(str, input().split())
    distance = int(distance)
    
    if direction == "R":
        distance += offset
        for i in range(offset, distance):
            n_list[i] = 1
        offset = distance
    else:
        distance = offset - distance
        for i in range(distance, offset):
            n_list[i] = 2
        offset = distance

cnt1 = 0
cnt2 = 0

for num in n_list:
    if num == 2:
        cnt1 += 1
    elif num == 1:
        cnt2 += 1

print(cnt1, cnt2)