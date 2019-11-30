import numpy as np
# Create a 5 by 5 matrix with rand numerical elements and store it to variable X
X = np.random.random((5,5))
print("")
# Get the element-wise mean of the matrix X and store it to variable x 
x = X.mean()
# Get the element-wise standard deviation  and store it to variable r
r = X.std()
# Normalize matrix X using the formula Z = (X-x)/r and store the normalized matrix to Z
Z = (X-x)/r
# Compare the Original Matrix to the Normalized Matrix
print("Matrix X:")
print(X)
print("")
print("Normalized X:")
print(Z)
np.save("X_normalized.npy",Z)