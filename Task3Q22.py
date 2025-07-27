def matrix_multiply(A, B):
    # Dimensions check
    if len(A[0]) != len(B):
        raise ValueError("Columns of A must match rows of B")
    
    rows_A = len(A)
    cols_B = len(B[0])
    common = len(B)
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            total = 0
            for k in range(common):
                total += A[i][k] * B[k][j]
            result[i][j] = total
    
    return result

# Example usage
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
product = matrix_multiply(A, B)
print(product)  # [[58, 64], [139, 154]]
