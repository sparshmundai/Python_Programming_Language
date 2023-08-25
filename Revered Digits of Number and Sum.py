#write python program to print reversed digits of number and their sum
num1 = int(input("Please type a number: "))
num2 = num1
reverse = 0
total = 0
while num2 != 0:
        Digit = num2 % 10
        num2 = num2 // 10
        reverse = reverse * 10 + Digit
        total = total + Digit
        
print("Reversed Digits of Number: ",reverse)
print("Sum of Numbers: ",total)
        
