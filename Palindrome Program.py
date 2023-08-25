#Write a python program to check the number is palindrome of not
num1 = 9876
num2 = num1
Rev = 0

while (num2 >= 1):
    Digit = num2 % 10       # % (Modulus),it gives a last digit of number
    print("Digit", Digit)

    Rev = Rev * 10 + Digit
    print("Rev", Rev)

    num2 = num2 // 10       # // (floor Division),it gives a starting digits of number expect last digit
    print("Num2", num2, "\n")
    
if (num1 == Rev):
    print("The Number {} is a Palindrome Number".format(num1))
else:
    print("The Number {} is not a Palindrome Number".format(num1))


