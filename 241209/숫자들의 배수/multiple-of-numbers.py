n = int(input())
arr.append(n)

# 입력받은 정수의 배수를 배열에 저장
for i in range(1, 10):
	a = arr[i - 1] + arr[0]
	arr.append(a)

for elem in arr:
    print(elem, end=" ")
    if elem % 5 == 0:
	    cnt += 1
        if cnt == 2:
            break

    