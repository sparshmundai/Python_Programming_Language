#Write a program to convert decimal to octal number 
num1 = int(input("please type a number: "))
quotient = num1
binary = ""
while quotient != 0:
    remainder = quotient % 8
    quotient = quotient // 8
    binary = str(remainder) + binary
print("the number {} of binary is {} ".format(num1, binary))
