import MyMath as MM
num = int(input("Enter Number : "))
print("Choose 1 to find Factors")
print("Choose 2 to find Sum Of Digits")
print("Choose 3 to Check Armstrong Number")
print("Choose 4 to Check Palindrome Number")
opt = int(input("Choose Option [1/2/3/4] : "))
if opt==1:
    MM.factor(num)
elif opt==2:
    print("Sum of digits of",num,"is",MM.SumOfDigit(num))
elif opt==3:
    if MM.IsArmstrong(num):
        print(num,"is Armstrong Number")
    else: print(num,"is not Armstrong Number")
elif opt==4:
    if MM.IsPalindrome(num):
        print(num,"is Palindrome Number")   
    else: print(num,"is not Palindrome Number")
