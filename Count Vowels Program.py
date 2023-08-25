#Write a python program to count vowels in string
str1 = input("please type a line: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for letter in str1:
      if letter in vowels:
            count = count + 1
print("{} vowels present in {}".format(count, str1))
