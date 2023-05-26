def partial_pivot(A, b):
    n = len(A)
    
    # index vector for changing the order of the rows
    o = [i for i in range(n)]
    
    for k in range(n - 1):
        # Find the row with the largest absolute value in column i
        max_row = k
        for j in range(k+1, n):
            if abs(A[o[j]][k]) > abs(A[o[max_row]][k]):
                max_row = j
        
        o[k], o[max_row] = o[max_row], o[k]
        
        for i in range(k + 1, n):
            factor = A[o[i]][k] / A[o[k]][k]
            b[o[i]] -= b[o[k]] * factor
            for j in range(k, n):
                A[o[i]][j] -= A[o[k]][j] * factor
                
    # Backward substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[o[i]] / A[o[i]][i]
        for j in range(i+1, n):
            x[i] -= A[o[i]][j] * x[j] / A[o[i]][i]
    
    return x, o, A, b

A = [[1,1,0,1], [2,1,-1,-1],[-1,-2,3,-1],[3,-1,-1,2]]
b = [2,1,4,-3]
x, o, A, b = partial_pivot(A, b)
#plotPolynomial(polynomial, x)
print(f'x: {x}, vetor o: {o}, A: {A}, b: {b}')