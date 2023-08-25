#Write a program to print GCD of two given numbers
a = int(input("please type a first number: "))
b = int(input("please type a second number; "))
x = 1
while(x <= a and x <= b):
    if (a % x==0 and b % x==0):
        gcd = x
    x = x + 1
print("Greatest Common Divisor of {} and {} is {}".format(a,b,gcd))
