num = int(input("enter the number: "))
fact = 1
for x in range(1,num+1):
    print("x",x)
    fact = fact * x
    print("fact",fact)
print("Factorial: ",fact)

