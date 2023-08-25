#Write a python program to print factors of number

user = int(input("Please provide a value: "))
print("Factor of Numbers")
for x in range(1, user+1):
        if user % x == 0:
                print("Factor: ",x)
