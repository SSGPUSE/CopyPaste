def IsPrime(n):
    flag=1
    for i in range(2,n//2+1):
        if n%i==0:
            flag=0
            break
    return flag

def IsPerfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return n==sum


