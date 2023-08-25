#Write a python program to identify whether a string is palindrome or not
#define function which return true if str is palindrome otherwise false
#abcba = rev(abcba)
def palin(str):
    revstr = str[::-1]
    if revstr == str:
       return True
    else:
        return False
    
instr = input("Please gve a string: ")
result = palin(instr)
print("The string {} is a palindrome {}".format(instr,result))

