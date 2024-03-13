a, o, c = map(str, input().split())

n1 = int(a)
n2 = int(c)

def check(n1, n2,a,o,c):
    ans = 0
    if o == "+":
        ans = n1 + n2
        print(a + " " + o + " " + c + " = " + str(ans) )
    elif o == "-":
        ans = n1 - n2
        print(a + " " + o + " " + c + " = " + str(ans) )
    elif o == "*":
        ans = n1 * n2
        print(a + " " + o + " " + c + " = " + str(ans) )
    elif o == "/":
        ans = n1 // n2
        print(a + " " + o + " " + c + " = " + str(ans) )
    else:
        return False
check(n1, n2,a,o,c)