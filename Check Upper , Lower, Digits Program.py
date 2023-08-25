#Write a python program to check how many upper,lower,digit character in line
line = input("please enter a line: ")
up = lw = digits = 0
for char in line:
    if char.islower():
        lw = lw + 1
    elif char.isupper():
        up = up + 1
    elif char.isdigit():
        digits = digits + 1
print("Upper character = {}, Lower character = {}, Digits character = {}".format(up, lw, digits))
