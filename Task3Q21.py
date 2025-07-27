def matrix_addition(A, B):
    rows = len(A)
    cols = len(A[0])
    # Optional: check if B has same dims
    C = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return C

# Example usage:
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
]
C = matrix_addition(A, B)
for row in C:
    print(row)
