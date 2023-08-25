#Write a python program to print pattern
#   *
#  * *
# * * *
#* * * *
rows  = int(input("type a number: "))
for x in range(1,rows+1):
      print(" "*rows, end="")
      print("x "*x)
      rows = rows - 1
