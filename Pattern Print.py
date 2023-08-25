#Write a program to print pattern
#1
#22
#333
#4444
#55555
num = int(input("Type a number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end="")
    print("")
    
#Write a program to print pattern
#1
#12
#123
#1234
#12345
num = int(input("Type a number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")

