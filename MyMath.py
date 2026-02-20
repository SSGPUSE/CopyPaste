def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")

def SumOfDigit(n):
    sum = 0
    while n > 0:
        rem = n%10
        sum += rem
        n //=10
    return sum

def IsArmstrong(n):
    temp = n 
    nod = 0
    while n > 0:    
        rem = n%10
        nod+=1
        n //=10
    n = temp
    sum = 0
    while n >0:
        rem = n%10
        sum += rem**nod
        n //=10
    return temp==sum

def IsPalindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rem = n%10
        rev = rev*10+rem
        n //=10
    return temp==rev
