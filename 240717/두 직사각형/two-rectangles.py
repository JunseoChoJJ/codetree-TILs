x1,y1,x2,y2 = map(int, input().split())
a1,b1,a2,b2 = map(int, input().split())


if x2 < a1 and y2 < b1 and b2 < y1 and a2 < x1:
    print("nonoverlapping")
else:
    print("overlapping")