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

    A = [[0.448,0.832,0.193],[0.421,0.784,-0.207],[-0.319,0.884,0.279]]
    b = [1,0,0]
    res, b = gaussElimination(A, b)
    printMatrix(res)
    print(b)

def printMatrix(A):
    for i in range(len(A)):
        print(A[i])

if __name__ == "__main__":
    main()
