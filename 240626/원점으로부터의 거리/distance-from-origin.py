class Num:
    def __init__(self, total, num):
        self.total=total
        self.num=num
nums=[]
n = int(input())
def get_dist_from_origin(x,y):
    return abs(x) + abs(y)


for i in range(1, n+1):
    x, y = map(int, input().split())
    nums.append(Num(get_dist_from_origin(x,y), i))

nums.sort(key=lambda x: (x.total, x.num))

for num in nums:
    print(num.num)