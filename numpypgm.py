import numpy as np

# Create a 1-dimensional NumPy array from a Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("Original 1D array:", arr1)

# Perform element-wise operations
arr_plus_one = arr1 + 1
print("Array after adding 1 to each element:", arr_plus_one)

arr_multiplied = arr1 * 2
print("Array after multiplying each element by 2:", arr_multiplied)

# Create a 2-dimensional NumPy array (matrix)
arr2 = np.array([[10, 20, 30], [40, 50, 60]])
print("\nOriginal 2D array (matrix):\n", arr2)

# Get the shape of the array
print("Shape of 2D array:", arr2.shape)

# Access elements using indexing
print("Element at row 0, column 1:", arr2[0, 1])

# Perform matrix addition with another array
arr3 = np.array([[1, 1, 1], [2, 2, 2]])
arr_sum = arr2 + arr3
print("Sum of two 2D arrays:\n", arr_sum)

# Calculate the mean of the array
mean_value = np.mean(arr1)
print("\nMean of arr1:", mean_value)
