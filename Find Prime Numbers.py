#Write python program to print prime numbers between 500 and 1500
num1 = int(input("please type first number: "))
num2 = int(input("please type second number: "))
total = 0
for x in range(num1,num2+1):
      prime = 1
      for y in range(2,x):
            if x%y ==0:
                  prime = 0
                  break
      if prime == 1:
            print(x)
            total = total + x            
print("Sum of the prime numbers is {}".format(total)) 


                  
