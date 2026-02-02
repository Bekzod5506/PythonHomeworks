import numpy as np

print("1) Vector from 10 to 49")
v = np.arange(10, 50)
print(v)

print("\n2) 3x3 matrix from 0 to 8")
m1 = np.arange(9).reshape(3, 3)
print(m1)

print("\n3) 3x3 identity matrix")
identity = np.eye(3)
print(identity)

print("\n4) 3x3x3 random array")
arr_3d = np.random.rand(3, 3, 3)
print(arr_3d)

print("\n5) 10x10 random array with min and max")
arr_10 = np.random.rand(10, 10)
print(arr_10)
print("Min:", arr_10.min())
print("Max:", arr_10.max())

print("\n6) Random vector of size 30 and mean")
vec30 = np.random.rand(30)
print(vec30)
print("Mean:", vec30.mean())

print("\n7) Normalize a 5x5 random matrix")
mat5 = np.random.rand(5, 5)
normalized = (mat5 - mat5.min()) / (mat5.max() - mat5.min())
print(normalized)

print("\n8) Multiply 5x3 by 3x2 matrix")
A = np.random.rand(5, 3)
B = np.random.rand(3, 2)
product1 = np.dot(A, B)
print(product1)

print("\n9) Dot product of two 3x3 matrices")
M1 = np.random.rand(3, 3)
M2 = np.random.rand(3, 3)
dot_product = np.dot(M1, M2)
print(dot_product)

print("\n10) Transpose of a 4x4 matrix")
mat4 = np.random.rand(4, 4)
transpose = mat4.T
print(transpose)

print("\n11) Determinant of a 3x3 matrix")
mat_det = np.random.rand(3, 3)
det = np.linalg.det(mat_det)
print(det)

print("\n12) Matrix product A (3x4) and B (4x3)")
A2 = np.random.rand(3, 4)
B2 = np.random.rand(4, 3)
product2 = np.dot(A2, B2)
print(product2)

print("\n13) Matrix-vector product")
matrix3 = np.random.rand(3, 3)
vector3 = np.random.rand(3)
result_mv = np.dot(matrix3, vector3)
print(result_mv)

print("\n14) Solve Ax = b")
A3 = np.random.rand(3, 3)
b = np.random.rand(3)
x = np.linalg.solve(A3, b)
print(x)

print("\n15) Row-wise and column-wise sums")
mat5x5 = np.random.rand(5, 5)
row_sum = mat5x5.sum(axis=1)
col_sum = mat5x5.sum(axis=0)
print("Matrix:\n", mat5x5)
print("Row sums:", row_sum)
print("Column sums:", col_sum)

