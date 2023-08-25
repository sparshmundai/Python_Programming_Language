#Write a python program to Matrix Multiplication

import numpy as np
#2x3 matrix
a = np.array([[1,2,3], [4,5,6]])

#3x2 matrix
b = np.array([[2,4], [6,8], [10, 12]])
product = a @ b
print(product)
