#write a python program to sort list manually
list1 = [50,60,10,8,1,6,12]

for j in range(0,len(list1)-1):
        for i in range(j+1,len(list1)):
                if list1[j] >= list1[i]:
                        temp = list1[j]
                        list1[j] = list1[i]
                        list1[i] = temp
print(list1)
