import numpy as np

# Create a 2D array
arr2D = np.array([[1, 1, 2], [3, 2, 1], [3, 3, 2], [1, 2, 2]])

# Get the unique values in the array
unique_values = np.unique(arr2D)

# Compute the row-wise counts of unique values
row_wise_counts = np.apply_along_axis(lambda x: np.bincount(x, minlength=len(unique_values)), axis=1, arr=arr2D)

print(row_wise_counts)
