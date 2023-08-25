def myfact(num):
    if(num == 0):
        return 1
    else:
        return (num * myfact(num-1))

num = int(input("enter the number: "))
num2 = myfact(num)
print("The {} number of factorial is {}".format(num,num2))
