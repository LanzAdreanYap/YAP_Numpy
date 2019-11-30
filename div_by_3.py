import numpy as np
# Create an array with elements containing numbers from 1 to 100 and reshape the array to a 10x10 matrix and store it to m
M = np.arange(1,101).reshape(10,10)
# Change each numerical element of the matrix to the square of its value and store it to msqrd
msqrd = M**2
# Determine the elements in the new matrix, msqrd, that are divisible by 3
div = msqrd[msqrd%3 == 0]
print("")

# Display the Matrix M
print("Matrix M:")
print(msqrd)
print("")
# Display the elements of the Matrix that are divisible by 3
print("Within the matrix consisting the squares of the first 100 positive integers")
print("The elements that are divisible by 3 are:")
print("")
print(div)

# Save the the resulting array 
np.save('div_by_3', div)
