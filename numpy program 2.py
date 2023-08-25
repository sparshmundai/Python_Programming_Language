import numpy as np
arr1 = np.array([[111,2200,3330],[444,555,102],[777,888,999]])
print("Numpy Array \n")
print(arr1,"\n")
arr2 = arr1.max()
print("First highest number in array:",arr2)


temp = 0
for x in np.nditer(arr1):
    if(x<arr2):
        temp = x
    
print("Second highest number in array",temp)

