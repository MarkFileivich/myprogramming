
def matrix_multiply(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")
    
    # Create result matrix (rows of A x columns of B)
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Multiply matrices
    for i in range(len(A)):          # rows of A
        for j in range(len(B[0])):   # columns of B
            for k in range(len(B)):  # rows of B / columns of A
                result[i][j] += A[i][k] * B[k][j]
    
    return result



