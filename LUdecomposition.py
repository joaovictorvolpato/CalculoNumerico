#Code for implementing LU decomposition method for solving linear systems

#LU method, is build upon the idea that any matrix can be decomposed into a product of a lower 
#triangular matrix and an upper triangular matrix. This is called LU decomposition. 
#The LU decomposition is a factorization of a matrix A into a product of a lower triangular matrix L and an upper triangular matrix U.

def LUdecomposition(A):
    n = len(A)
    #build lower triangular matrix
    Lmatrix = [[0 for i in range(n)] for j in range(n)]
    Umatrix = [[0 for i in range(n)] for j in range(n)]
    #k Lmatrix column Umatrix row 
    for k in range(n):
        for i in range(k,n): 
            Lmatrix[i][k]=A[i][k]-sum([Lmatrix[i][t]*Umatrix[t][k] for t in range(0,k)])
        Umatrix[k][k] = 1
        for j in range(k+1,n):
            Umatrix[k][j]=(A[k][j]-sum([Lmatrix[k][t]*Umatrix[t][j] for t in range(0,k)]))/Lmatrix[k][k]

    return Umatrix, Lmatrix 

def solveLinearSystem(A, b):
    U, L = LUdecomposition(A)
    #solve Ly = b
    y = [0 for i in range(len(b))]
    y[0] = b[0]/L[0][0]
    for i in range(1,len(b)):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i)))/L[i][i]

    print(y)
    #solve Ux = y
    x = [0 for i in range(len(b))]
    x[-1] = y[-1]/U[-1][-1]
    for k in range(len(b)-1, -1, -1):
        x[k] = (y[k] - sum([U[k][j] * x[j] for j in range(k+1, len(b))]))

    print(x)
    return x

def main():
    A = [[1,1,2],[3,-5,1],[2,1,-1]]
    b = [27,-9,1]
    print(solveLinearSystem(A, b))

def printMatrix(A):
    for i in range(len(A)):
        print(A[i])
    

if __name__ == "__main__":
    main()