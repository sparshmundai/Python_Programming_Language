#write a python program to print prime numbers between 500 and 1500
print("Prime Numbers")
for x in range(500,1501):
      prime = 1
      for y in range(2,x):
            if x%y == 0:
                  prime = 0
                  break
      if prime == 1:
            print(x)

                  
