# Input 2x2 matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Sum
matrix_sum = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

# Product
matrix_product = [
    [A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
    [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]
]

# Sort rows by row sum
matrix_product_sorted = sorted(matrix_product, key=lambda row: sum(row))

print("Matrix A:", A)
print("Matrix B:", B)
print("Sum:", matrix_sum)
print("Product:", matrix_product)
print("Sorted Product by row sum:", matrix_product_sorted)
