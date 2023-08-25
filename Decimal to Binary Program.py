#Write a program to convert Decimal to Binary Number
num1 = int(input("please type a number: "))
quotient = num1
binary = ""
while quotient != 0:
    remainder = quotient % 2
    quotient = quotient // 2
    binary = str(remainder) + binary
print("the number {} of binary is {} ".format(num1, binary))
