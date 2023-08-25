import numpy as np
arr1 = np.arange(27).reshape(3,3,3)
print("Numpy Array \n")
print(arr1,"\n")
arr2 = arr1.max()
print("First highest number in array:",arr2)


temp = 0
for x in np.nditer(arr1):
    if(x<arr2):
        temp = x
print("Second highest number in array",temp)
