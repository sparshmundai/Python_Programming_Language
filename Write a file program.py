#Write a python program to write content in file
fp1 = open("new.txt","w")

#input from user to type a line
input1 = input("Type a line 1: ")
input2 = input("Type a line 2: ")
input3 = input("Type a line 3: ")
input4 = input("Type a line 4: ")
input5 = input("Type a line 5: ")

#write lines in file
fp1.write(input1)
fp1.write("\n")
fp1.write(input2)
fp1.write("\n")
fp1.write(input3)
fp1.write("\n")
fp1.write(input4)
fp1.write("\n")
fp1.write(input5)

#close the file
fp1.close()



