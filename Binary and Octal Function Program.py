#Write a function program to convert Decimal to Binary number
def dtob(num):
    if num > 1:
        dtob(num // 2)
    print(num % 2, end="") 
    
number = int(input("Enter Decimal Number: "))
dtob(number)


#Write a functtion program to Convert Decimal to Octal Number
def octal(num):
    if num > 1:
        octal(num // 8)
    print(num % 8, end="")
    
number = int(input("Enter Decimal Number: "))
octal(number)




