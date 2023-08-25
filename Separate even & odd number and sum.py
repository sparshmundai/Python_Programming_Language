list1 = []
num1 = int(input("Please type a number: "))
while num1 !=-9:
      list1.append(num1)
      num1 = int(input("enter a number: "))
etotal = 0
ototal = 0
for x in list1:
      if x%2 == 0:
            etotal = etotal + 1
      else:
            ototal = ototal + 1
print("Sum of Odd numbers {} and even numbers {} ".format(ototal  ,etotal))
            
