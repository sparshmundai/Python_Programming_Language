#User defined function 
def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))

#Take input from uesr    
num = int(input("How many number do you print: "))

#Print the sequence wise number
if(num <= 0):
    print("Incorrect Number")
else:  
   print("Fibonacci SeriesS:")  
   for x in range(num):  
       print(fibo(x))  
