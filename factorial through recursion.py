#Program for factorial through recursion
def fact(num):
    if num == 1:
        return 1
    else:
        return(num*fact(num-1))

#input through user 
num1 = int(input("Type number to calculate factorial : "))
result = fact(num1)

print("Factorial of {} is {} ".format(num1, result))
