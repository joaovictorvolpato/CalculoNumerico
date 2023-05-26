#Code for solving linear systems with the Gauss method


def gaussElimination(A,b):
    n = len(A)
    for k in range(n):
        for i in range(k+1, n):
            eliminationfactor = A[i][k]/A[k][k]
            b[i] -= b[k] * eliminationfactor
            for j in range(k, n):
                A[i][j] -= A[k][j] * eliminationfactor

    #back substitution
    x = [0 for i in range(n)]
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - sum(A[k][j] * x[j] for j in range(k+1, n)))/A[k][k]


    return A, x

def main():

    A = [[1,1,0,1],[2,1,-1,-1],[-1,-2,3,-1],[3,-1,-1,2]]
    b = [2,1,4,-3]
    res, b = gaussElimination(A, b)
    printMatrix(res)
    print(b)

def printMatrix(A):
    for i in range(len(A)):
        print(A[i])

if __name__ == "__main__":
    main()
