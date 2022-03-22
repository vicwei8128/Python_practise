# importing the numpy module
import numpy as np

# Input array of non-negative integers
inp_arr = np.array([1, 2, 5, 6, 2, 1, 8, 8, 8])

x = np.bincount(inp_arr)
print("Output of bincount is: ", x)

# printing the size of output bin
print("\nSize of output bin: ", len(x))