A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("A : " , A)
print("B: " ,B)

print("*"*10)

#1 sum of matrix

sum_matrix = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Sum of A and B:", sum_matrix)

print("*"*10)

#Sum of All Elements in One Matrix
total_sum = sum(sum(row) for row in A)
print("Sum of all elements in A:", total_sum)

print("*"*10)

#Sum of Each Row and Each Column
row_sums = [sum(row) for row in A]
col_sums = [sum(A[i][j] for i in range(len(A))) for j in range(len(A[0]))]
print("Row sums:", row_sums)
print("Column sums:", col_sums)

print("*"*10)

#Multiply 2 matrix
product = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print("Product of A and B:", product)

print("*"*10)

#max and min element
flat = [elem for row in A for elem in row]
print("Max:", max(flat))
print("Min:", min(flat))

print("*"*10)

#major diagonal 
major_diag = [A[i][i] for i in range(min(len(A), len(A[0])))]
print("Major diagonal:", major_diag)

print("*"*10)

#minor diagonal
minor_diag = [A[i][len(A[0]) - 1 - i] for i in range(min(len(A), len(A[0])))]
print("Minor diagonal:", minor_diag)

print("*"*10)

#check if square matrix
is_square = len(A) == len(A[0])
print("Is square matrix:", is_square)



