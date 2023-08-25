#Write a python program to calulate factorial numbers
n = int(input("Enter number: "))
num = n
fact = 1
while (n!=1):
    fact = fact * n
    n = n-1
print("Factorial of the given number {} is {} ".format(num,fact))
