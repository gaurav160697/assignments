#Create a null vector of size 10 but the fifth value which is 1.

import numpy as np

null_vector = np.zeros(10)
null_vector[4] = 1

print(null_vector)

#Create a vector with values ranging from 10 to 49.

import numpy as np

vector = np.arange(10, 50)

print(vector)

#Create a 3x3 matrix with  values ranging from 0 to 8

import numpy as np

matrix = np.arange(9).reshape(3, 3)

print(matrix)

#Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np

array = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(array)[0]

print(non_zero_indices)

#Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

array = np.random.rand(10, 10)

min_value = np.min(array)
max_value = np.max(array)

print("Minimum value:", min_value)
print("Maximum value:", max_value)

# Create a random vector of size 30 and find the mean value.

import numpy as np

vector = np.random.rand(30)

mean_value = np.mean(vector)

print("Mean value:", mean_value)

