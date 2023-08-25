#write a python program to print pattern
#*
#**
#***
#****
#*****
n = int(input("provide a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print("")


#Write a python program to print pattern reversed
#*****
#****
#***
#**
#*
n = int(input("provide a number: "))
for i in reversed(range(1,n+1)):
    for j in range(1,i+1):
        print("*", end="")
    print("")
