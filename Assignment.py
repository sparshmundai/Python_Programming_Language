for i in range (1,5):
    for j in range (1,4):
        print (i,j)
        
#creating list from string
str = "this is dia64"
list2 = list(str)
print(list2)

#creating list from string
list3 = str.split()
print(list3)


str1 = "today it is very humid and hot"
vowels = ['a','e','i','o','u']
nvowels = 0
for chr in str1:
    if chr in vowels:
        nvowels = nvowels + 1
print("no of vowels in the srting {} is {}".format(str1,nvowels))

#Range function in list
print(list(range(10)))
print(list("this is dia64"))
list1 = list(range(2,20,5))
print("The Length of the list1 {} is {}".format(list1, len(list1)))
      
#Traverse list using for loop
for i in range(len(list1)):
    print(list1[i]*list1[i])

#traverse list using while loop
i = 0
while i < len(list1):
     print(list1[i]*list1[i])
     i = i+1

#print even numbers
print("print even numbers in list")
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i = 1
while i < len(list2):
    print(list2[i], end =" ")
    i = i+2

#print odd numbers
print("print odd numbers in list")
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i = 0
while i < len(list2):
    print(list2[i], end =" ")
    i = i+2

#FIND THE SUM OF THE ELEMENT IN LIST USING FOR LOOP
list1 = list(range(2,20,2))
print(list1)
sum = 0
for x in list1:
    sum = sum + x
print("Sum of elements in the list is = {} and average is {}".format
(sum, sum/len(list1)))
