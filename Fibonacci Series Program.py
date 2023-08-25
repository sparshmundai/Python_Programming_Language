#write a program to Print Fibonacci Series
a= int(input("type a first number: "))
b= int(input("type a second number: "))
print(a)
print(b)
result = a+b
print(result)
while result <= 1000:
    a=b
    b=result
    result = a+b
    print(result)
