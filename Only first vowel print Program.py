#Write a python program to count only one vowels in string
str1 = input("Please type a line : ")
vowels = ['a','e','i','o','u', 'A','E', 'I','O','U']
position = 0
for ch in str1:
      position = position + 1
      if ch in vowels:
            print("Vowel {} is at position {} ".format(ch, position))
            break
