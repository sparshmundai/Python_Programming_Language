line = input("Enter the sentence: ")
print(line,"\n")
myset = tuple(line)
final = {}


#Alphabet count in string program
for x in myset:
    counts = 0
    for y in line:
        if (x == y):
            counts = counts +1
    final[x] = counts
print(final,"\n")


# same number alphabet count in string program
mydict = dict()
mydict2 = dict()
for keys,values in final.items():
    if values in mydict:
        mydict[values].append(keys)
    else:
        mydict[values] = [keys]
print(mydict)


for k, v in final.items():
    mydict2[v] = mydict2.get(v, []) + [k]
print(mydict)
        
        

