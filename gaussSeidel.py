#Python code for implementing Gauss-Seidel method

def gaussSeidel(A,b,precision):
    n = len(A)
    x = [0 for i in range(n)] # initial guess
    xnew = [0 for i in range(n)] # new values
    error = 1
    ite = 0
    while error > precision:
        for i in range(n):
            soma1 = 0
            soma2 = 0
            for j in range(i):
                if j < i:
                    soma1 += A[i][j] * xnew[j]
            for j in range(i+1, n):
                if j > i:
                    soma2 += A[i][j] * x[j]
            xnew[i] = (b[i] - soma1 - soma2)/A[i][i]
            #print(f"x{i}: {xnew[i]} ", end="")
        
        error = max([abs(xnew[i] - x[i]) for i in range(n)])
        #print(error)
        x = xnew[:]
        ite += 1
    return x, ite


def gaussSeidelrelx(A, b, w, precision):
    n = len(A)
    x = [0 for i in range(n)] # initial guess
    xnew = [0 for i in range(n)] # new values
    error = 1
    ite = 0
    while error > precision:
    #for k in range(10):
        #xnew = [0 for i in range(n)]
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i][j] * xnew[j]
            xnew[i] = (1-w)*x[i] + w*(b[i] - soma)/A[i][i]
            print(f"x{i}: {xnew[i]} ", end="")
        print()

        #print(x)
        #print(xnew)
        error = max([abs(xnew[i] - x[i]) for i in range(n)])
        print(error)
        x = xnew[:]
        ite += 1
    return x, ite
    

def main():
    A = [[4,1,2],[1,2,1],[1,0.1,1]]
    b = [1,4,-3]
    #print(gaussSeidelrelx(A, b, 0.80, 1e-10))
    print(gaussSeidel(A, b, 10e-6))

if __name__ == "__main__":
    main()
