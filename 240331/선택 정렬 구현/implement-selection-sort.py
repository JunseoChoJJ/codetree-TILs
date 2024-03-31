n = int(input())
n_list = list(map(int, input().split()))

def insertion(n_list):

    for i in range(len(n_list) - 1):
        mins = i
        for j in range(i + 1, len(n_list) - 1):
            if n_list[j] < n_list[mins]:
                mins = j
        tmp = n_list[i]
        n_list[i] = n_list[mins]
        n_list[mins] = tmp
        #print(n_list)
insertion(n_list)

for num in n_list:
    print(num, end = ' ')