#write a python program to remove "The or the" in a string
str1 = "The Dhillon Theatre is now the Fun Republic"
str2 = str1.replace("The","")
print(str2)
str1  = str2.replace("the","")
print(str1)
str2 = str1.strip()
print(str2)

#write a python program to count letter in a string
str1 = "Twinkle Twinkle little star"
c = intput("type character which you want to ount: ")
chrcnt = 0
for x in str1:
      if x == c.upper() or x==.lower():
            

