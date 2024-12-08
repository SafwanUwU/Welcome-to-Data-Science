import numpy as np

matrix_a = np.arange(9, dtype=float).reshape(3, 3)
print("Matrix 'matrix_a':")
print(matrix_a)

array_b = np.array([10, 10, 10])
print("\nArray 'array_b':")
print(array_b)

print("\nElement-wise addition of 'matrix_a' and 'array_b':")
print(np.add(matrix_a, array_b))

print("\nElement-wise subtraction of 'array_b' from 'matrix_a':")
print(np.subtract(matrix_a, array_b))

print("\nElement-wise multiplication of 'matrix_a' and 'array_b':")
print(np.multiply(matrix_a, array_b))

print("\nElement-wise division of 'matrix_a' by 'array_b':")
print(np.divide(matrix_a, array_b))
