#Python code for implementing Gauss-Jacobi method


def gaussJacobi(A, b, precision):
    n = len(A)
    x = [0 for i in range(n)] # initial guess
    xnew = [0 for i in range(n)] # new values
    error = 1
    while error > precision:
    #for k in range(10):
        #xnew = [0 for i in range(n)]
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * x[j]
            xnew[i] = (b[i] - soma)/A[i][i]
            print(f"x{i}: {xnew[i]} ", end="")
        print()

        #print(x)
        #print(xnew)
        error = max([abs(xnew[i] - x[i]) for i in range(n)])
        print(error)
        x = xnew[:]
    return x

def main():
    A = [[3,-1,-1],[1,3,1],[2,-2,4]]
    b = [1,5,4]
    print(gaussJacobi(A, b, 1e-10))

if __name__ == "__main__":
    main()