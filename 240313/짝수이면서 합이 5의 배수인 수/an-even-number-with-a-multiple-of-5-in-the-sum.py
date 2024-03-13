n = int(input())

def check(n):
    word = list(str(n))
    wor = list(map(int, word))
    
    if n % 2 == 0 and sum(wor) % 5 == 0:
        print("Yes")
    else:
        print("No") 

check(n)