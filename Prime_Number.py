def IsPalindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rem = n%10
        rev += rev*10+rem
        n //=10
    if temp==rev:
        print("true")
        
IsPalindrome(121)