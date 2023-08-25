#Program to copied odd lines from one file to another 
fp1 = open("file.txt", "r")
fp2 = open("oddlines.txt","w+")
lineno = 1
for line in fp1.readlines():
      if lineno%2 !=0:
            fp2.write(line)
      lineno = lineno + 1
fp1.close()
fp2.close()      
print("Oddlines file is created and the content is copied.")


#Program to copied even lines from one file to another 
fp1 = open("file.txt", "r")
fp2 = open("evenlines.txt","w+")
lineno = 1
for line in fp1.readlines():
      if lineno%2 ==0:
            fp2.write(line)
      lineno = lineno + 1
fp1.close()
fp2.close()      
print("Evenlines file is created and the content is copied.")


